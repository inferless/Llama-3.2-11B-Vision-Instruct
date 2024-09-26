INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["Describe this image?"]
    },
    "image_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://huggingface.co/datasets/huggingface/documentation-images/resolve/0052a70beed5bf71b92610a43a52df6d286cd5f3/diffusers/rabbit.jpg"]
    },
    "max_new_tokens": {
        'datatype': 'INT32',
        'required': False,
        'shape': [1],
        'example': [50]
    }
}
