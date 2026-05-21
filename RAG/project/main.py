import gradio as gr

def add_numbers(num1, num2):
    return num1 + num2

inferface = gr.Interface(fn=add_numbers, inputs=["number", "number"], outputs="number")
inferface.launch()

