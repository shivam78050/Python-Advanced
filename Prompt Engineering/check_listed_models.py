import google.generativeai as genai

genai.configure(api_key="AIzaSyCNZDAuuh5y1l29Q70fV9BLOA51JPLR97Y")

for model in genai.list_models():
    print(model.name)