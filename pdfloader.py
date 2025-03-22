from langchain_community.document_loaders import PyPDFLoader

pdf_loader = PyPDFLoader('resource/demo.pdf')
documents = pdf_loader.load()
print(documents)