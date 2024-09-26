# Tutorial - Deploy Llama-3.2-11B-Vision-Instruct using Inferless
The Llama 3.2 11B Vision Instruct model is part of Meta's latest series of large language models that introduce significant advancements in multimodal AI capabilities, allowing for both text and image inputs.

## TL;DR:
- Deployment of Llama-3.2-11B-Vision-Instruct model using [Transformers](https://github.com/huggingface/transformers).
- You can expect an average latency of `2.44 sec`. This setup has an average cold start time of `10.60 sec`.
- Dependencies defined in `inferless-runtime-config.yaml`.
- GitHub/GitLab template creation with `app.py`, `inferless-runtime-config.yaml` and `inferless.yaml`.
- Model class in `app.py` with `initialize`, `infer`, and `finalize` functions.
- Custom runtime creation with necessary system and Python packages.
- Model import via GitHub with `input_schema.py` file.
- Recommended GPU: NVIDIA A100 for optimal performance.
- Custom runtime selection in advanced configuration.
- Final review and deployment on the Inferless platform.

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Add Your Hugging Face Auth Token
Go into the `inferless.yaml` and replace `<YOUR_HUGGINGFACE_ACCESS_TOKEN>` with your hugging face api key. Make sure to check the repo is private to protect your hugging face key.

### Create a Custom Runtime in Inferless
To access the custom runtime window in Inferless, simply navigate to the sidebar and click on the Create new Runtime button. A pop-up will appear.

Next, provide a suitable name for your custom runtime and proceed by uploading the inferless-runtime-config.yaml file given above. Finally, ensure you save your changes by clicking on the save button.

### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the `Add a custom model` button.

- Select `Github` as the method of upload from the Provider list and then select your Github Repository and the branch.
- Choose the type of machine, and specify the minimum and maximum number of replicas for deploying your model.
- Configure Custom Runtime ( If you have pip or apt packages), choose Volume, Secrets and set Environment variables like Inference Timeout / Container Concurrency / Scale Down Timeout
- Once you click “Continue,” click Deploy to start the model import process.
  
Refer [this link](https://docs.inferless.com/integrations/git-custom-code/git--custom-code) for more information on model import.


---
## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in inputs. Refer to [input](#input) for more.

```python
def infer(self, inputs):
    image_url = inputs["image_url"]
    prompt = inputs["prompt"]
    max_new_tokens = inputs.get("max_new_tokens",30)
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu by setting `self.model = None`.

For more information refer to the [Inferless docs](https://docs.inferless.com/).
