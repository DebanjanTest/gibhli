<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ghibli Style Transfer | Transform Your Images</title>
    <style>
        :root {
            --primary: #4a86e8;
            --secondary: #7aa9f5;
            --accent: #ff9c6b;
            --light: #f7f9fc;
            --dark: #2c3e50;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: var(--light);
            color: var(--dark);
            line-height: 1.6;
        }
        
        header {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 2rem 0;
            text-align: center;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .hero {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 60vh;
            text-align: center;
            padding: 4rem 1rem;
            background: url('/api/placeholder/1200/600') center center/cover no-repeat;
            background-color: rgba(0, 0, 0, 0.4);
            background-blend-mode: overlay;
            color: white;
        }
        
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin-bottom: 2rem;
        }
        
        .btn {
            display: inline-block;
            background-color: var(--accent);
            color: white;
            padding: 12px 30px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        }
        
        .features {
            padding: 5rem 0;
            background-color: white;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .feature-card {
            background-color: var(--light);
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
        }
        
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: var(--primary);
        }
        
        .examples {
            padding: 5rem 0;
            background-color: var(--light);
        }
        
        .examples-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .example-card {
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .example-img {
            width: 100%;
            height: 300px;
            object-fit: cover;
        }
        
        .example-text {
            padding: 1.5rem;
            background-color: white;
        }
        
        .app-section {
            padding: 5rem 0;
            background-color: white;
            text-align: center;
        }
        
        .upload-container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            background-color: var(--light);
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .upload-area {
            border: 2px dashed var(--primary);
            border-radius: 10px;
            padding: 3rem;
            margin-bottom: 2rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .upload-area:hover {
            background-color: rgba(74, 134, 232, 0.05);
        }
        
        .style-options {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
            margin: 2rem 0;
        }
        
        .style-option {
            padding: 0.5rem 1rem;
            border: 2px solid var(--primary);
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .style-option.active {
            background-color: var(--primary);
            color: white;
        }
        
        .result-container {
            display: none;
            max-width: 800px;
            margin: 2rem auto;
        }
        
        .result-comparison {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }
        
        .result-img {
            width: 100%;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        footer {
            background-color: var(--dark);
            color: white;
            padding: 3rem 0;
            text-align: center;
        }
        
        .footer-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin: 2rem 0;
        }
        
        .footer-link {
            color: white;
            text-decoration: none;
        }
        
        .footer-link:hover {
            text-decoration: underline;
        }
        
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            
            .result-comparison {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Ghibli AI</h1>
            <p>Transform your photos into Studio Ghibli-inspired masterpieces</p>
        </div>
    </header>
    
    <section class="hero">
        <h1>Experience the Magic of Studio Ghibli</h1>
        <p>Upload any image and our AI will transform it into a beautiful Studio Ghibli style artwork. Choose from different iconic Ghibli film styles.</p>
        <a href="#app" class="btn">Try it Now</a>
    </section>
    
    <section class="features">
        <div class="container">
            <h2 class="section-title" style="text-align: center; margin-bottom: 3rem;">Features</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🎨</div>
                    <h3>Multiple Ghibli Styles</h3>
                    <p>Choose from various iconic Ghibli films including Spirited Away, My Neighbor Totoro, Howl's Moving Castle, and Princess Mononoke.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Fast Processing</h3>
                    <p>Our advanced AI model processes your images quickly, delivering high-quality results in seconds.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💎</div>
                    <h3>High Resolution</h3>
                    <p>Get beautiful high-resolution images that maintain the quality and detail of your original photos.</p>
                </div>
            </div>
        </div>
    </section>
    
    <section class="examples">
        <div class="container">
            <h2 class="section-title" style="text-align: center; margin-bottom: 3rem;">Example Transformations</h2>
            <div class="examples-grid">
                <div class="example-card">
                    <img src="/api/placeholder/400/300" alt="Before-After Spirited Away Style" class="example-img">
                    <div class="example-text">
                        <h3>Spirited Away Style</h3>
                        <p>Dreamy, ethereal watercolor look with vibrant colors and magical elements.</p>
                    </div>
                </div>
                <div class="example-card">
                    <img src="/api/placeholder/400/300" alt="Before-After Totoro Style" class="example-img">
                    <div class="example-text">
                        <h3>My Neighbor Totoro Style</h3>
                        <p>Soft, pastoral scenes with lush green landscapes and gentle lighting.</p>
                    </div>
                </div>
                <div class="example-card">
                    <img src="/api/placeholder/400/300" alt="Before-After Howl's Moving Castle Style" class="example-img">
                    <div class="example-text">
                        <h3>Howl's Moving Castle Style</h3>
                        <p>Steam-punk inspired aesthetic with detailed machinery and fantastical elements.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <section id="app" class="app-section">
        <div class="container">
            <h2 class="section-title" style="margin-bottom: 1rem;">Transform Your Image</h2>
            <p style="margin-bottom: 2rem;">Upload your photo and choose a Ghibli style to transform it</p>
            
            <div class="upload-container">
                <div class="upload-area" id="uploadArea">
                    <h3>Drag & Drop Your Image Here</h3>
                    <p>or</p>
                    <input type="file" id="fileInput" style="display: none;">
                    <button class="btn" onclick="document.getElementById('fileInput').click()">Select File</button>
                </div>
                
                <div>
                    <h3>Choose a Style</h3>
                    <div class="style-options">
                        <div class="style-option active" data-style="spirited-away">Spirited Away</div>
                        <div class="style-option" data-style="totoro">My Neighbor Totoro</div>
                        <div class="style-option" data-style="howls-castle">Howl's Moving Castle</div>
                        <div class="style-option" data-style="mononoke">Princess Mononoke</div>
                    </div>
                </div>
                
                <button class="btn" id="transformBtn" disabled>Transform Image</button>
            </div>
            
            <div class="result-container" id="resultContainer">
                <h3>Your Transformed Image</h3>
                <p>Here's your image in beautiful Ghibli style</p>
                
                <div class="result-comparison">
                    <div>
                        <h4>Original</h4>
                        <img src="/api/placeholder/400/300" alt="Original Image" class="result-img" id="originalImg">
                    </div>
                    <div>
                        <h4>Ghibli Style</h4>
                        <img src="/api/placeholder/400/300" alt="Transformed Image" class="result-img" id="transformedImg">
                    </div>
                </div>
                
                <div style="margin-top: 2rem;">
                    <a href="#" class="btn" id="downloadBtn">Download Image</a>
                    <button class="btn" style="background-color: var(--primary); margin-left: 1rem;" id="newTransformBtn">Create Another</button>
                </div>
            </div>
        </div>
    </section>
    
    <footer>
        <div class="container">
            <h2>Ghibli AI</h2>
            <p>Transform your photos into Studio Ghibli-inspired masterpieces</p>
            
            <div class="footer-links">
                <a href="#" class="footer-link">About</a>
                <a href="#" class="footer-link">Privacy Policy</a>
                <a href="#" class="footer-link">Terms of Service</a>
                <a href="#" class="footer-link">Contact</a>
            </div>
            
            <p>&copy; 2025 Ghibli AI. All rights reserved.</p>
        </div>
    </footer>
    
    <script>
        // Simple front-end functionality for demonstration
        document.addEventListener('DOMContentLoaded', function() {
            const fileInput = document.getElementById('fileInput');
            const uploadArea = document.getElementById('uploadArea');
            const transformBtn = document.getElementById('transformBtn');
            const resultContainer = document.getElementById('resultContainer');
            const originalImg = document.getElementById('originalImg');
            const transformedImg = document.getElementById('transformedImg');
            const newTransformBtn = document.getElementById('newTransformBtn');
            const styleOptions = document.querySelectorAll('.style-option');
            
            // Style selection
            styleOptions.forEach(option => {
                option.addEventListener('click', function() {
                    styleOptions.forEach(o => o.classList.remove('active'));
                    this.classList.add('active');
                });
            });
            
            // File upload handling
            fileInput.addEventListener('change', function(e) {
                if (e.target.files && e.target.files[0]) {
                    const reader = new FileReader();
                    
                    reader.onload = function(event) {
                        uploadArea.innerHTML = `<img src="${event.target.result}" alt="Uploaded Image" style="max-width: 100%; max-height: 300px;">`;
                        originalImg.src = event.target.result;
                        transformBtn.disabled = false;
                    }
                    
                    reader.readAsDataURL(e.target.files[0]);
                }
            });
            
            // Drag and drop functionality
            uploadArea.addEventListener('dragover', function(e) {
                e.preventDefault();
                uploadArea.style.backgroundColor = 'rgba(74, 134, 232, 0.1)';
            });
            
            uploadArea.addEventListener('dragleave', function() {
                uploadArea.style.backgroundColor = '';
            });
            
            uploadArea.addEventListener('drop', function(e) {
                e.preventDefault();
                uploadArea.style.backgroundColor = '';
                
                if (e.dataTransfer.files && e.dataTransfer.files[0]) {
                    fileInput.files = e.dataTransfer.files;
                    const event = new Event('change');
                    fileInput.dispatchEvent(event);
                }
            });
            
            // Transform button
            transformBtn.addEventListener('click', function() {
                // In a real application, here you would send the image to your API
                // For demo purposes, we'll just show a mock result
                resultContainer.style.display = 'block';
                
                // Simulate loading
                transformedImg.src = '/api/placeholder/400/300';
                
                // In a real app, you would replace this with actual API call
                setTimeout(() => {
                    window.scrollTo({
                        top: resultContainer.offsetTop,
                        behavior: 'smooth'
                    });
                }, 500);
            });
            
            // New transform button
            newTransformBtn.addEventListener('click', function() {
                resultContainer.style.display = 'none';
                uploadArea.innerHTML = `
                    <h3>Drag & Drop Your Image Here</h3>
                    <p>or</p>
                    <button class="btn" onclick="document.getElementById('fileInput').click()">Select File</button>
                `;
                transformBtn.disabled = true;
                
                window.scrollTo({
                    top: document.getElementById('app').offsetTop,
                    behavior: 'smooth'
                });
            });
        });
    </script>
</body>
</html>
