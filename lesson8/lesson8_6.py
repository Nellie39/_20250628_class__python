import gradio as gr
from google import genai

client = genai.Client()

#建立gradio Blocks架構
with gr.Blocks() as demo:
   gr.Markdown("## 公司內部機器人")
   #建立輸入框
   input_text = gr.Textbox(label="請在下方輸入問題", placeholder="您的問題...", submit_btn=True)

   #建立gradio.Accordion
   with gr.Accordion("**常見問題**", open=True):
      gr.Examples(
         examples=[
            "請問台灣的首都是哪裡？",
            "請問台灣的國土面積有多大？",
            "請問台灣的人口有多少？",
            "請問台灣的官方語言是什麼？",
            "請問現在最強大的AI模型是什麼？",
         ],
         inputs=input_text
      )
   
   #建立輸出框
   output_text = gr.Textbox(
      label="機器人回覆", 
      placeholder="機器人會在這裡回答你的問題", 
      interactive=False)
   
   @input_text.submit(inputs=[input_text],outputs=[output_text])
   def respond(message):
       # 在這裡處理用戶輸入的訊息
       respone = client.models.generate_content(
           model="gemini-2.5-flash",
           contents=[message]       
       )
       return respone.text

demo.launch()