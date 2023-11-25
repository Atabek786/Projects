# Imaginify: Text-to-Art AI
#### Description:
TextIntoImage AI is a Python project that harnesses the power of the OpenAI API to convert text prompts into captivating images and generate variations of images. This project demonstrates how to interact with the OpenAI API to create visual representations based on textual input.

## Features:

1. **Text-to-Image Conversion:** Utilizing the `main()` function, users can input a text prompt, which the OpenAI API transforms into an image. The resulting image is then saved in JSON format, accompanied by relevant metadata.

2. **Image Variation Generation:** The project includes the `openai.Image.create_variation()` function, allowing users to take an existing image stored in the "responses" directory and generate multiple image variations. These variations are also saved in JSON format for future use.

## Requirements:
- Python is installed on your system.
- Python libraries : `openai`, `os`, `json`, `base64`, and `pathlib`.
- An OpenAI API key is required. Set it as an environment variable with the name `OPENAI_API_KEY` to access the OpenAI API for image-related tasks.
## How to Use:

1. Clone this repository to your local machine.
2. Install the required Python libraries by running the following command in your terminal or command prompt:  pip install openai
3. Set up your OpenAI API key as an environment variable. Replace `<YOUR_API_KEY>` with your actual API key:

- **For Windows:**
  ```
  setx OPENAI_API_KEY "<YOUR_API_KEY>"
  ```

- **For macOS and Linux:**
  ```
  export OPENAI_API_KEY="<YOUR_API_KEY>"
  ```

Note: You may need to restart your terminal or command prompt for the changes to take effect.

4. Execute the script by running the following command: python your_script_name.py

- To perform text-to-image conversion, provide a text prompt when prompted by the script.
- For generating image variations, ensure you have an existing image JSON file in the "responses" directory, and the file name is correctly referenced in the script.

5. The generated images and variations will be saved in the "images" directory for future reference.

## Note:

- Comply with the terms and conditions of the OpenAI API when using this project.
- Basic understanding of Python and working with APIs is assumed. If you encounter any issues, refer to the OpenAI API documentation or seek support from the OpenAI community.

Feel free to customize and expand this project to suit your specific requirements. 
