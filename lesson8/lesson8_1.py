import gradio as gr

def greet(name, intensity):
    return "哈囉你好嗎, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch(share=True)