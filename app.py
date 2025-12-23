from roboflow import Roboflow
import gradio as gr

# Roboflow setup
rf = Roboflow(api_key="erXiXrjNNI9iTS2d8LBW")
model = rf.workspace("emotion-detection-woffv") \
          .project("student_behavior_analysis") \
          .version(1) \
          .model

# Function to predict
def predict_image(image):
    image.save("temp_upload.png")
    result = model.predict("temp_upload.png", confidence=40, overlap=30)
    result.save("output.png")
    return "output.png", result.json()

# Gradio Blocks layout
with gr.Blocks() as demo:
    # Header
    gr.Markdown("<h1 style='text-align:center; color:#4B0082;'>Student Behavior Emotion Detection</h1>")
    gr.Markdown("<p style='text-align:center; color:#555;'>Upload a student image and get real-time emotion prediction!</p>")
    
    # Two-column layout: input and output
    with gr.Row():
        with gr.Column(scale=1, min_width=300):
            upload_image = gr.Image(type="pil", label="Upload Image", interactive=True)
            predict_btn = gr.Button("Predict", variant="primary")
        with gr.Column(scale=1, min_width=300):
            output_image = gr.Image(type="filepath", label="Predicted Image")
            output_json = gr.JSON(label="Prediction Result")
    
    # Connect button
    predict_btn.click(fn=predict_image, inputs=upload_image, outputs=[output_image, output_json])

# Launch the app with theme
demo.launch(theme="default")  # or "huggingface", "soft", etc.
