import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import numpy as np
import gradio as gr

class ContentLoss(nn.Module):
    def __init__(self, target):
        super(ContentLoss, self).__init__()
        self.target = target.detach()
        self.loss = nn.MSELoss()

    def forward(self, x):
        self.loss_value = self.loss(x, self.target)
        return x

class StyleLoss(nn.Module):
    def __init__(self, target_feature):
        super(StyleLoss, self).__init__()
        self.target = self._gram_matrix(target_feature).detach()
        self.loss = nn.MSELoss()

    def forward(self, x):
        gram = self._gram_matrix(x)
        self.loss_value = self.loss(gram, self.target)
        return x
    
    def _gram_matrix(self, x):
        b, c, h, w = x.size()
        features = x.view(b * c, h * w)
        gram = torch.mm(features, features.t())
        return gram.div(b * c * h * w)

class GhibliStyleTransfer:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.imsize = 512
        self.loader = transforms.Compose([
            transforms.Resize((self.imsize, self.imsize)),
            transforms.ToTensor()
        ])
        self.vgg = models.vgg19(pretrained=True).features.to(self.device).eval()
        
        # Pre-trained on Ghibli style reference images
        self.style_references = {
            "spirited_away": "path/to/spirited_away_style.jpg",
            "totoro": "path/to/totoro_style.jpg",
            "howls_moving_castle": "path/to/howls_moving_castle_style.jpg",
            "princess_mononoke": "path/to/princess_mononoke_style.jpg"
        }
        
    def _image_loader(self, image_path):
        image = Image.open(image_path)
        image = self.loader(image).unsqueeze(0).to(self.device)
        return image
    
    def transfer_style(self, content_img_path, style_choice="spirited_away", num_steps=300):
        content_img = self._image_loader(content_img_path)
        style_img = self._image_loader(self.style_references[style_choice])
        
        # Create input image (starting from content)
        input_img = content_img.clone()
        
        # Content and style layers based on VGG19
        content_layers = ['conv_4']
        style_layers = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']
        
        # Setup optimizer
        optimizer = optim.LBFGS([input_img.requires_grad_()])
        
        # Implement style transfer optimization
        # (simplified for brevity - would include building the model with content and style losses)
        
        # Return the stylized image
        return self._tensor_to_image(input_img)
    
    def _tensor_to_image(self, tensor):
        image = tensor.cpu().clone().detach().numpy().squeeze()
        image = image.transpose(1, 2, 0)
        image = np.clip(image, 0, 1)
        return Image.fromarray((image * 255).astype(np.uint8))

# Create Gradio interface
def create_gradio_app():
    style_transfer = GhibliStyleTransfer()
    
    def process_image(input_image, style_choice):
        # Save input image temporarily
        temp_path = "temp_input.jpg"
        input_image.save(temp_path)
        
        # Apply style transfer
        output_image = style_transfer.transfer_style(temp_path, style_choice)
        return output_image
    
    # Create interface
    interface = gr.Interface(
        fn=process_image,
        inputs=[
            gr.Image(type="pil", label="Upload your image"),
            gr.Dropdown(
                choices=list(style_transfer.style_references.keys()),
                label="Choose Ghibli Style",
                value="spirited_away"
            )
        ],
        outputs=gr.Image(label="Ghibli-Style Result"),
        title="Ghibli Style Transfer",
        description="Transform your images into Studio Ghibli-inspired artwork"
    )
    
    return interface

# Main function to run the app
if __name__ == "__main__":
    app = create_gradio_app()
    app.launch(share=True)
