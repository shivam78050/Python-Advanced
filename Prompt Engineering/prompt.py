
import keras_hub
import itertools
import pandas as pd
import google.generativeai as genai

# -----------------------------
# STEP 1: Generate Ground Truth
# -----------------------------

fico_values = [751, 825, 900]
inq_values = [2, 50, 99]

expected_output = [
    (f, n, "Declined", "INQUIRIES")
    for f, n in itertools.product(fico_values, inq_values)
]
##########
print("EXPECTED OUTPUT:\n")

for row in expected_output:
    print(row)



prompt = """
You are given a business rule.

Rule:
If FICO > 750 and FICO <= 900
and NO_INQ >= 2 and NO_INQ <= 99

then:
DECISION_CD = Declined
DECISION_DESC = INQUIRIES

Use these values:

FICO:
- 751
- 825
- 900

NO_INQ:
- 2
- 50
- 99

Generate ALL possible combinations.

Output format:
(FICO, NO_INQ, 'Declined', 'INQUIRIES')

Return ONLY tuples.
No explanation.
"""


# Replace with your Gemini API key
GOOGLE_API_KEY = "AIzaSyBssC8klaE_pzDp-cgbMgEikhwWD4R0i8c"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

gemini_response = model.generate_content(prompt)

print("\n\nGEMINI OUTPUT:\n")
print(gemini_response.text)
