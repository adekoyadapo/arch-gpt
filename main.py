from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import streamlit as st
import os, io, glob
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

st.title("CLOUD ARCHITECTURE DIAGRAM APP")
st.write("Create any diagram of your choice")
input_text = st.text_area("Ask anything about your task")

# Define the prompt template
ts = """
Your job is to write the python code using Diagram module to generate a cloud architecture diagram for 
    {steps} information only, don't use any other information.
    Only generate the code as output, nothing extra.
    For reference, to import ELB in the code, always use:
    from diagrams.aws.network import ELB
    Code:
    """
pt = ChatPromptTemplate.from_template(ts)

# Load the Azure OpenAI model using environment variables for API keys
# Azure OpenAI LLM setup
llm = AzureChatOpenAI(
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_version="2024-02-01",
    max_tokens=4096,
    temperature=0.0
)

# Chain to handle input and output
qa_chain = LLMChain(llm=llm, prompt=pt)

if input_text is not None:
    btn = st.button("Submit")
    if btn:
        response = qa_chain.invoke({"steps": input_text})
        data = response["text"]
        code = data.replace("python", "")
        code = code.replace("`", "")
        cwd = os.getcwd()

        # Remove old png files
        files = glob.glob(cwd + "/*.png")
        for file in files:
            os.remove(file)
        
        # Write the generated code to a Python file
        with io.open("codesample.py", "w", encoding="utf-8") as f1:
            f1.write(code)
        
        # Run the Python file to generate the diagram
        os.system("python codesample.py")

        # Check for generated image files
        files = glob.glob(cwd + "/*.png")
        if len(files) == 1:
            st.image(files[0])