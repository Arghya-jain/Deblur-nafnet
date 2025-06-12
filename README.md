# Image Deblurring using Generative AI for Mobile

## About
This project is part of the **Samsung PRISM** initiative and focuses on enhancing blurred images using AI. The model, **NAFNet (Nonlinear Activation Free Network)**, simplifies traditional deep learning architectures by removing activation functions like ReLU and Sigmoid. This results in a more efficient model with reduced computational costs while maintaining high performance. NAFNet achieves **state-of-the-art results** in image deblurring, making it a reliable and fast solution for mobile applications.

## Installation and Setup

### Prerequisites
To set up the project, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/Arghya-jain/Deblur-nafnet.git
   ```
2. Navigate to the project directory:
   ```sh
   cd project_folder
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Quick Start
To quickly deblur an image, use the following command:
```sh
python NAFNet/demo.py -opt options/test/REDS/NAFNet-width64.yml --input_path uploads/101.png --output_path outputs/deblur_img.png
```

## How to Start

1. **Clone the Project**
   ```sh
   git clone https://github.ecodesamsung.com/suhasbs-22cse/Deblring.git
   ```

2. **Move to the Working Directory**
   ```sh
   cd PROJECT_FOLDER
   ```

3. **Add the Trained Model**
   - Download the pre-trained model from the links below:

| Dataset | Download Link |
|---------|--------------|
| **GoPro** | [Download](https://drive.google.com/file/d/1S0PVRbyTakYY9a82kujgZLbMihfNBLfC/view) |
| **REDS**  | [Download](https://drive.google.com/file/d/14D4V4raNYIOhETfcuuLI3bGLB-OYIv6X/view) |

   - Create a new folder inside the `NAFNet` directory:
     ```sh
     mkdir -p NAFNet/experiments
     ```
   - Place the downloaded model inside `NAFNet/experiments`:
     ```sh
     mv REDS_.pth NAFNet/experiments/
     ```

4. **Run the Application**
   ```sh
   python app.py
   ```
   - After execution, a local URL link will appear in the terminal.
   - Open the link in a browser to access the interface.
   - Upload a blurred image and click on the **"Enhance Image"** button.
   - The processed deblurred image will be displayed.

5. **Image Storage**
   - Uploaded images are stored in the **`uploads`** folder.
   - Processed (deblurred) images are stored in the **`outputs`** folder.

## Model Performance

| Model Name               | Dataset | PSNR  | SSIM  |
|--------------------------|---------|-------|-------|
| NAFNet-GoPro-width32     | GoPro   | 32.8705 | 0.9606 |
| NAFNet-REDS-width64      | REDS    | 29.0903 | 0.8671 |

---


