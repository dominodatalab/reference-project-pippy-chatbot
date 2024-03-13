# Pippy Chatbot

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
