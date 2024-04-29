# Pippy Chatbot Template
Pippy is a Retrieval-Augmented Generation (RAG) Chatbot that utilizes vector embeddings of 
[Domino documentation](https://docs.dominodatalab.com/) in combination with a Large Language Model (LLM) like ChatGPT.
In this repository, you can find a template to build your RAG chatbot off of, including source files
to embed your texts and deploy the app.

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
### Dataset
You can create a Domino Dataset containing your own metadata file and PDFs, similar to the sample files, to be embedded 
into a vector database. Then, reference it in `docs_embedder.ipynb` so Pippy can answer questions based on your data!

### Data Source
Set up a vector database with an index as a 
[Domino Data Source](https://docs.dominodatalab.com/en/latest/user_guide/fbb41f/data-source-connectors/) in your 
Domino deployment to store and retrieve embeddings. You can use any of the supported vector databases such as 
[Pinecone](https://docs.dominodatalab.com/en/latest/user_guide/5c64ef/connect-to-pinecone/) or
[Qdrant](https://docs.dominodatalab.com/en/latest/user_guide/c2364c/connect-to-qdrant/). 

Note: Use an index with dimension 1536 if using OpenAI (to match OpenAI's text-embedding-ada-002 model dimensions).

### AI Gateway
[Domino AI Gateway](https://docs.dominodatalab.com/en/latest/admin_guide/cce362/ai-gateway/) 
allows you to securely access external LLMs with access control and auditing. Create two AI Gateway endpoints for 
embeddings and chat. The embeddings endpoint allows you to access an embeddings model to create a vector embedding of 
a chunk of text while the chat endpoint allows you to query a chat model to generate responses based on the embeddings.

To create an AI Gateway endpoint , use the
[aigateway](https://docs.dominodatalab.com/en/latest/api_guide/8c929e/rest-api-reference/#_createGatewayEndpoint)
endpoint in the Domino REST API as shown below:

#### Embeddings Endpoint
```
curl -d '{     
    "endpointName":"embeddings",
    "endpointType":"llm/v1/embeddings",
    "endpointPermissions":{"isEveryoneAllowed":true,"userIds":[]},
    "modelProvider":"openai",
    "modelName":"text-embedding-ada-002",
    "modelConfig":{"openai_api_key":"<OpenAI_API_Key>"}
}' -H "X-Domino-Api-Key:<Domino_API_Key>" -H "Content-Type: application/json" -X POST https://<Deployment_Base_Url>/api/aigateway/v1/endpoints
```
#### Chat Endpoint
```
curl -d '{
    "endpointName":"chat",
    "endpointType":"llm/v1/chat",
    "endpointPermissions":{"isEveryoneAllowed":true,"userIds":[]},
    "modelProvider":"openai",
    "modelName":"gpt-3.5-turbo",
    "modelConfig":{"openai_api_key":"<OpenAI_API_Key>"}
}' -H "X-Domino-Api-Key:<Domino_API_Key>" -H "Content-Type: application/json" -X POST https://<Deployment_Base_Url>/api/aigateway/v1/endpoints
```
Note: Please refer to [Domino AI Gateway](https://docs.dominodatalab.com/en/latest/admin_guide/cce362/ai-gateway/) docs
for the must up-to-date create endpoint commands.

### MLflow (Automatically Integrated)
We log the user queries, system prompt, conversation summary, search filters, and responses in the "Experiments" 
tab of your Domino project, which implements MLflow. The logic for this resides in `chatbot.py` and 
can be modified to suit your logging requirements. No additional steps are needed to use MLflow as it 
already comes with your Domino deployment.

To learn more about MLflow in Domino, check out our 
[article on tracking and monitoring](https://docs.dominodatalab.com/en/latest/user_guide/da707d/track-and-monitor-experiments/).

### Datasets (Optional)
You can create [Datasets](https://docs.dominodatalab.com/en/latest/user_guide/0a8d11/create-and-modify-datasets/) in your Domino project
and populate it with the data you want to create vector embeddings from (PDFs of articles and metadata file). This can
then be mounted automatically when running a [Domino Workspace](https://docs.dominodatalab.com/en/latest/user_guide/e6e601/launch-a-workspace/).

### Environment Requirements
The "Pippy RAG Chatbot Environment" is automatically created with this project template. This will be 
available in the "Environment" tab of your Domino project and accessible to your workspaces and jobs. You may reference
this environment if you want to build your own environment with the same dependencies.

### Hardware Requirements
This project works with a standard small-sized hardware tier, such as the small-k8s tier on all Domino deployments.

## Development in Domino Deployment
To develop and test your changes, create a workspace with the above environment definition.
Then:

1. Change ports in `app.sh` to any free port such as `8887` (the default `8888` is the port used 
when the app is published in Domino)
2. Run `./app.sh`
3. Go to `https://{domino-host-url}/{domino-username}/{domino-project-name}/r/notebookSession/{runId}/proxy/8887/`
where `runId` can be found in the URL of the workspace.

## Deploying the App
1. Go to the "App" tab in you Domino project
2. Set the app title and any other configurations you wish to add such as a description and permissions
3. Click "Publish" to deploy the app in Domino!

See our article on [Publish an App](https://docs.dominodatalab.com/en/latest/user_guide/71635d/publish-apps/) 
for more detail on how to publish a variety of apps in Domino.