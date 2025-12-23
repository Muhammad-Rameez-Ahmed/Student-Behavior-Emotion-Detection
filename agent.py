# from roboflow import Roboflow
# import gradio as gr
# from transformers import pipeline

# # -----------------------------
# # 1️⃣ Roboflow Setup
# # -----------------------------
# rf = Roboflow(api_key="erXiXrjNNI9iTS2d8LBW")  # <-- Replace with your API key
# model = rf.workspace("emotion-detection-woffv") \
#           .project("student_behavior_analysis") \
#           .version(1) \
#           .model

# # -----------------------------
# # 2️⃣ Hugging Face LLM Setup
# # -----------------------------
# # You can use a text generation model like GPT-2, or better GPT-neo for local summarization
# summary_pipeline = pipeline("text-generation", model="gpt2")  # or any HF model

# # -----------------------------
# # 3️⃣ Prediction + Summary Function
# # -----------------------------
# def predict_and_summarize(image):
#     # Save uploaded image
#     image.save("outputs/temp_upload.png")
    
#     # Predict using Roboflow
#     result = model.predict("outputs/temp_upload.png", confidence=40, overlap=30)
#     result.save("outputs/output.png")
    
#     # Generate a behavior summary from prediction JSON
#     prediction_text = str(result.json())  # convert JSON to string
#     summary = summary_pipeline(
#         f"Analyze the student behavior from this prediction data and summarize key emotions and actions:\n{prediction_text}",
#         max_length=150,
#         do_sample=True
#     )[0]['generated_text']
    
#     # Save summary to file (optional)
#     with open("outputs/report.txt", "w") as f:
#         f.write(summary)
    
#     return "outputs/output.png", result.json(), summary

# # -----------------------------
# # 4️⃣ Gradio UI
# # -----------------------------
# with gr.Blocks() as demo:
#     gr.Markdown("<h1 style='text-align:center; color:#4B0082;'>Student Behavior Emotion Detection</h1>")
#     gr.Markdown("<p style='text-align:center; color:#555;'>Upload a student image and get emotion predictions & behavior summary!</p>")
    
#     with gr.Row():
#         with gr.Column(scale=1, min_width=300):
#             upload_image = gr.Image(type="pil", label="Upload Image")
#             predict_btn = gr.Button("Predict", variant="primary")
#         with gr.Column(scale=1, min_width=300):
#             output_image = gr.Image(type="filepath", label="Predicted Image")
#             output_json = gr.JSON(label="Prediction Result")
#             output_summary = gr.Textbox(label="Behavior Summary", lines=8)
    
#     predict_btn.click(
#         fn=predict_and_summarize, 
#         inputs=upload_image, 
#         outputs=[output_image, output_json, output_summary]
#     )

# # -----------------------------
# # 5️⃣ Launch
# # -----------------------------
# demo.launch(theme="default")
