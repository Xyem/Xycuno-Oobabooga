import random
import requests

class XycunoOobabooga:
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "host": ( "STRING", {
          "default": "http://127.0.0.1:5000",
        }),
        "prompt": ( "STRING", {
          "multiline": True,
          "default": """
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Describe an image in the same format as the Input but with similar concepts. Add, remove and substitute elements to make the description be 50 words or less.

### Input:
masterpiece, best quality, girl, fennec fox ears, flower field

### Response:
""".strip(),
        }),
        "seed":        ("INT",   {"default": 0,   "min": 0, "max": 0xffffffffffffffff}),
        "max_tokens":  ("INT",   {"default": 200, "min": 0, "max": 0xffffffffffffffff}),
        "temperature": ("FLOAT", {"default": 1.0, "min": 0, "max": 0xffffffffffffffff}),
        "top_p":       ("FLOAT", {"default": 0.9, "min": 0, "max": 0xffffffffffffffff}),
      }
    }

  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("response",)
  FUNCTION = "oobabooga"
  CATEGORY = "Xycuno/Oobabooga"

  def oobabooga(self, host, prompt, seed, max_tokens, temperature, top_p):
    url = "/v1/completions"
    url = host + url

    headers = {
        "Content-Type": "application/json"
    }

    data = {
      "prompt":      prompt,
      "max_tokens":  max_tokens,
      "temperature": temperature,
      "top_p":       top_p,
      "seed":        seed,
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    llm_response = response.json()['choices'][0]['text']

    return(llm_response, )
