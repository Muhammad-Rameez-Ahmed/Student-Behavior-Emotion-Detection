# from roboflow import Roboflow
# import gradio as gr
# import cv2
# import os
# from moviepy.editor import ImageSequenceClip

# # Roboflow setup
# rf = Roboflow(api_key="YOUR_API_KEY")
# model = rf.workspace("emotion-detection-woffv") \
#           .project("student_behavior_analysis") \
#           .version(1) \
#           .model

# # Create folders
# os.makedirs("frames", exist_ok=True)
# os.makedirs("output_frames", exist_ok=True)

# def predict_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     fps = int(cap.get(cv2.CAP_PROP_FPS))
#     frame_paths = []
#     out_paths = []

#     frame_count = 0

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_name = f"frames/frame_{frame_count}.jpg"
#         cv2.imwrite(frame_name, frame)
#         frame_paths.append(frame_name)

#         # Roboflow prediction
#         result = model.predict(frame_name, confidence=40, overlap=30)
#         output_frame = f"output_frames/out_{frame_count}.jpg"
#         result.save(output_frame)
#         out_paths.append(output_frame)

#         frame_count += 1

#     cap.release()

#     # Convert frames back to video
#     clip = ImageSequenceClip(out_paths, fps=fps)
#     output_video = "output_video.mp4"
#     clip.write_videofile(output_video, codec="libx264")

#     return output_video

# # Gradio UI
# with gr.Blocks() as demo:
#     gr.Markdown("<h1 style='text-align:center;'>Student Behavior Emotion Detection (Video)</h1>")

#     with gr.Row():
#         with gr.Column():
#             video_input = gr.Video(label="Upload Video")
#             predict_btn = gr.Button("Predict Video", variant="primary")
#         with gr.Column():
#             video_output = gr.Video(label="Output Video")

#     predict_btn.click(
#         fn=predict_video,
#         inputs=video_input,
#         outputs=video_output
#     )

# demo.launch()
