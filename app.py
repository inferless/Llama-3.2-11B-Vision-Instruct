import requests
import torch
from PIL import Image
from transformers import MllamaForConditionalGeneration, AutoProcessor

class InferlessPythonModel:
    def initialize(self):
        model_id = "meta-llama/Llama-3.2-11B-Vision-Instruct"
        self.model = MllamaForConditionalGeneration.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16,
            device_map="cuda",
        )
        self.processor = AutoProcessor.from_pretrained(model_id)

    def infer(self, inputs):
        image_url = inputs["image_url"]
        prompt = inputs["prompt"]
        max_new_tokens = inputs.get("max_new_tokens",30)
        
        messages = [
                    [
                        {
                            "role": "user", 
                            "content": [
                                {"type": "image"},
                                {"type": "text", "text": prompt}
                            ]
                        }
                    ],
                ]
        input_text = self.processor.apply_chat_template(messages, add_generation_prompt=True)
        image = Image.open(requests.get(image_url, stream=True).raw)
        inputs = self.processor(image, input_text, return_tensors="pt").to(self.model.device)
        
        output = self.model.generate(**inputs, max_new_tokens=max_new_tokens)
        output_text = self.processor.decode(output[0],skip_special_tokens=True)
        
        return {"generated_text":output_text}

    def finalize(self):
        self.model = None
