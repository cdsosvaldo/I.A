def call_gemini(prompt, image_data=None):
    import os
    import requests

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    
    contents = [{"parts": [{"text": prompt}]}]
    
    if image_data:
        contents[0]["parts"].append({
            "inlineData": {
                "mimeType": "image/jpeg",
                "data": image_data
            }
        })

    response = requests.post(url, params=params, headers=headers, json={"contents": contents})
    return response.json()