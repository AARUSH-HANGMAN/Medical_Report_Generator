import requests
import json


API_KEY = "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"


medical_text = """
Patient Name: John Doe
Age: 45
Blood Pressure: 140/90 mmHg
Blood Sugar: 180 mg/dL (Fasting)
Diagnosis: Type 2 Diabetes Mellitus, Hypertension
Medication: Metformin, Amlodipine
"""


url = "https://api.perplexity.ai/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


system_prompt = """
You are a professional medical assistant.

First, summarize the report clearly and briefly, highlighting key data like diagnosis, vitals, and medications.

Then, provide a simple, patient-friendly explanation of what the report means and what steps the patient might need to take.
"""

user_prompt = f"""
Here is a medical report:

{medical_text}

Please summarize and analyze this report.
"""


payload = {
    "model": "sonar",
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
}


response = requests.post(url, headers=headers, json=payload)


if response.status_code == 200:
    reply = response.json()
    output = reply['choices'][0]['message']['content']
    print("\n--- Summary & Analysis ---\n")
    print(output)
else:
    print(f"Error {response.status_code}: {response.text}")
