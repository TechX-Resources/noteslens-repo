import os
import base64
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
      
endpoint = os.getenv("ENDPOINT_URL", "https://rayd-mffvp8jp-eastus2.cognitiveservices.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "o3-mini")
      
# Initialize Azure OpenAI client with Entra ID authentication
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2025-01-01-preview",
)


# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
chat_prompt = [
    {
        "role": "developer",
        "content": [
            {
                "type": "text",
                "text": "You are an assistant that checks curriculum coverage. \nYou will be given a teacher's lesson text and a list of educational standards. \nFor each standard:\n- Decide if it is \"covered\", \"partially covered\", or \"missing\".\n- If partially covered or missing, suggest 2–3 specific improvements the teacher could add.\n\nOutput your results in JSON with this structure:\n[\n  {\n    \"standard_id\": \"string\",\n    \"status\": \"covered | partially covered | missing\",\n    \"suggestions\": [\"string\", \"string\"]\n  },\n  ...\n]\nKeep your responses concise and factual. Do not invent standards."
            }
        ]
    }
]

# Include speech result if speech is enabled
messages = chat_prompt

completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_completion_tokens=40000,
    stop=None,
    stream=False
)

print(completion.to_json())