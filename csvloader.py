from langchain_community.document_loaders.csv_loader import CSVLoader

csv_loader = CSVLoader(file_path='resource/demo.csv')
documents = csv_loader.load()
print(documents)