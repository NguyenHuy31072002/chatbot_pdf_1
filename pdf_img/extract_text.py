import os
from dotenv import load_dotenv
from together import Together

# Load biến môi trường từ file .env
load_dotenv()



def extract_text_with_prompt_from_image(image_url,prompt):
    # Lấy API key từ biến môi trường và cấu hình Google Gemini API
    api_key = os.getenv("TOGETHER_API_KEY")
    client = Together(api_key=api_key)
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
        messages=[
            {
                    "role": "user",
                    "content": [
                            {
                                    "type": "text",
                                    "text": prompt if prompt else "Extract the text from the image"
                            },
                            {
                                    "type": "image_url",
                                    "image_url": {
                                            "url": image_url
                                    }
                            }
                    ]
            }
    ],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>","<|eom_id|>"],
    )
    # print('response',response)
    return response.choices[0].message.content if response.choices else "Unable to process the image with the provided prompt."









