# Pippy Chatbot

## What's in here
### embed_gen
This folder contains `docs_embedder.ipynb`, which turns PDF documents into embeddings in a vector database such as Pinecone.
It also comes with sample files including the `pages.csv` metadata file and the `pdfs` folder.

The columns of the `pages.csv` are categories that form the metadata of an embedded text to filter a query by. 
For example, you can filter the chatbot to only search for relevant docs for Domino 5.8.0.
`pdfs` contain a sample PDF of an article that can be used to embed its text.  

### chatbot.py
This contains the main business logic of retrieving a user query, doing a search filtered by metadata in a vector database
for relevant context, and combining this context with ChatGPT for a relevant response.

### Other
* `app.sh` contains configuration logic
* `ui` includes frontend logic for rendering the app's sidebar with a description and filtering options
* `assets` folder contains an image of Pippy!

## Set-up
### Datasets

### Data Source

### AI Gateway

### Environment Definition
Use the following base image: `Domino Standard Environment Py3.9 R4.3` for Domino 5.10.0.

Additional Dockerfile instructions:
```
RUN pip install streamlit==1.31.1 pypdf==4.0.2 pinecone-client==3.1.0 ipywidgets==8.1.2 langchain==0.1.8
RUN pip install --user dominodatalab-data==5.10.1
RUN pip install --user pinecone-client==2.2.4
```

## Local Development

To develop and test your changes, create a workspace with the above environment definition.
Then:

1. Change ports in `app.sh` to `8887`
2. Run `./app.sh`
3. Go to `https://{domino-url}/{username}/{domino-project-name}/r/notebookSession/{runId}/proxy/8887/`
