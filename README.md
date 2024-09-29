# Infrastructure Architecture Diagram App

## Overview

This application, built using **Streamlit** and **Azure OpenAI**, allows you to create Python code for cloud architecture diagrams based on user input. It utilizes the **Langchain** framework with **Azure OpenAI's GPT-4 model** to generate the required Python code for cloud diagrams, which are created using the **Diagrams** module. 

The app accepts user input describing a cloud architecture and then generates the corresponding Python code using the **Diagrams** module to visualize the architecture. The generated diagram is automatically displayed in the app interface.

## Features

- **Streamlit-based UI**: Provides a simple interface for user input.
- **Azure OpenAI Integration**: Leverages the GPT-4 model from Azure OpenAI to generate Python code.
- **Automatic Diagram Generation**: Uses the `Diagrams` module to create cloud architecture diagrams.
- **Dynamic Rendering**: Automatically runs the generated Python code to create and display the architecture diagram.

## How It Works

1. The user inputs a request in the text area describing their cloud architecture diagram.
2. The app sends the user's input to the GPT-4 model via **Azure OpenAI**.
3. GPT-4 generates Python code using the **Diagrams** library.
4. The generated Python code is saved to a file, executed, and the diagram (saved as a `.png`) is displayed in the app.

## How to Run the Application

### Prerequisites

Before running the app, make sure you have installed the following dependencies.

### 1. Install Python dependencies:

Create a virtual environment and activate it:

```bash
# For macOS/Linux:
python3 -m venv env
source env/bin/activate

# For Windows:
python -m venv env
.\env\Scripts\activate
```

Then install the necessary Python libraries:

```bash
pip install -r requirements.txt
```

### 2. Install Graphviz

You also need **Graphviz**, which is required by the `diagrams` module. Install Graphviz based on your operating system:

#### **macOS**:
Install via **Homebrew**:

```bash
brew install graphviz
```

#### **Ubuntu**:
Install via **apt**:

```bash
sudo apt-get install graphviz
```

#### **Windows**:
1. Download the Graphviz installer from the official site: https://graphviz.gitlab.io/download/
2. Install it and add Graphviz to your system PATH.

### 3. Set up Environment Variables

Create a `.env` file in the root directory of the project with the following content:

```
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint_here
AZURE_OPENAI_DEPLOYMENT_NAME=your_azure_deployment_name_here
```

Replace the values of `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, and `AZURE_OPENAI_DEPLOYMENT_NAME` with your actual credentials from Azure OpenAI.

### 4. Run the Application

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will start, and you can interact with it via your web browser. Enter your cloud architecture task in the text area, and the app will generate and display the corresponding diagram.

## Example .env File

```env
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-openai-resource-name.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
```

## Example Usage

1. Run the app.
2. Enter a description such as:

    ```
    Create a cloud architecture with a load balancer (ELB), two EC2 instances, and an S3 bucket.
    ```
   
3. Click "Submit". The app will:
   - Use the GPT-4 model to generate Python code.
   - Run the code to generate a cloud architecture diagram.
   - Display the generated `.png` diagram in the app.

## Requirements

The following Python packages are needed:

```
streamlit
langchain-openai
langchain
openai
python-dotenv
diagrams
graphviz
```

Additionally, make sure **Graphviz** is installed on your system (refer to the instructions above).

---

This README should provide users with all the necessary steps to understand, install, and run the application.