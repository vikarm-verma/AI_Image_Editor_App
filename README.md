# AI Photo Editor

An AI-powered photo editing application built with **Python, Streamlit, LangChain, and Google Gemini**.

The application allows users to upload an image, describe the desired edit in natural language, and generate an AI-edited image.

## Features

- Upload an image from your computer
- Describe the required edit using a natural-language prompt
- Refine the user's instruction using LangChain and Gemini
- Edit the image using Gemini's image model
- Preview the edited image
- Download the edited image
- Basic input validation and error handling

## Technology Stack

- **Python** – Application development
- **Streamlit** – Web interface
- **Pillow** – Image handling
- **LangChain** – Prompt orchestration and refinement
- **Google Gemini** – AI text and image processing
- **python-dotenv** – Environment variable management

## Project Structure

```text
AI-Photo-Editor/
│
├── app.py
├── ai_editor.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── GUIDE.docx
```

### File Description

| File | Purpose |
|---|---|
| `app.py` | Streamlit user interface |
| `ai_editor.py` | LangChain prompt refinement and Gemini image-editing logic |
| `requirements.txt` | Required Python packages |
| `.env.example` | Template for environment variables |
| `.gitignore` | Files that should not be uploaded to GitHub |
| `README.md` | Project overview and quick-start instructions |
| `GUIDE.docx` | Detailed step-by-step project guide |

## Prerequisites

Before running the project, make sure you have:

- Python 3.10 or later
- A Google AI Studio / Gemini API key
- VS Code or another Python-compatible IDE

## Installation

### 1. Clone or Download the Project

Download or clone this repository and open the project folder in VS Code.

### 2. Create a Virtual Environment

Open the terminal in the project folder and run:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

Install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## API Key Setup

The application requires a Gemini API key.

### 1. Create the `.env` file

Copy `.env.example` and rename the copy to:

```text
.env
```

### 2. Add your API key

Open `.env` and add:

```env
GEMINI_API_KEY=your_google_ai_studio_api_key_here
```

The project also supports model configuration through environment variables:

```env
LANGCHAIN_TEXT_MODEL=gemini-2.5-flash
GEMINI_IMAGE_MODEL=gemini-3.1-flash-image
```

Do **not** upload `.env` to GitHub because it contains your private API key.

## Run the Application

After activating the virtual environment, run:

```bash
streamlit run app.py
```

Streamlit will start the application and provide a local URL in the terminal.

## How to Use

1. Open the Streamlit application.
2. Upload an image.
3. Enter an editing instruction.
4. Click **Generate Edited Image**.
5. Review the generated image.
6. Download the edited image if required.

### Example Prompts

```text
Remove the background and replace it with a modern office.
```

```text
Change the background to a sunset beach while keeping the person unchanged.
```

```text
Make the image look like a professional studio photograph.
```

```text
Convert the background into a clean minimalist setting.
```

## How LangChain Is Used

LangChain is used as the prompt-orchestration layer.

The application follows this flow:

```text
User Prompt
     ↓
LangChain + Gemini Text Model
     ↓
Refined Editing Instruction
     ↓
Gemini Image Model
     ↓
Edited Image
     ↓
Display / Download
```

LangChain does not directly edit the image. It helps refine and structure the user's instruction before the image-editing model processes it.

## Error Handling

The application validates the user's input and handles common errors such as:

- Empty prompts
- Very long prompts
- Missing API keys
- API/model errors
- Image-processing errors

User-friendly error messages are displayed in the Streamlit interface.

## Switching Models or Providers

The project is currently configured for Google Gemini.

Changing an AI provider is not always as simple as replacing the API key. Depending on the provider, you may need to update:

- Environment variables
- Python SDK imports
- LangChain integration
- Text model name
- Image model name
- API request format
- Response handling
- `requirements.txt`

Also note that some AI providers offer text models but do not provide image-editing capabilities. In that case, LangChain can still be used for prompt orchestration while a separate image-capable service handles the actual image editing.

Always check the current provider documentation before making these changes.

## GitHub Security

Do not commit sensitive or machine-specific files such as:

```text
.env
.venv/
__pycache__/
*.pyc
```

The `.env.example` file is safe to include because it contains placeholders rather than the actual API key.

## Detailed Guide

For complete step-by-step instructions, refer to:

**`GUIDE.docx`**

The guide covers environment setup, API configuration, application usage, LangChain integration, provider switching, troubleshooting, and GitHub best practices.

## License

This project is intended for educational and portfolio purposes.
