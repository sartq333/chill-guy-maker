import gradio as gr
from face_parsing import integration_with_meme

def replace_face(person_image, face_x, face_y, face_width, face_height):
    result_image = integration_with_meme(input_img_path=person_image, face_x=face_x, face_y=face_y, face_width=face_width, face_height=face_height)
    return result_image

interface = gr.Interface(
    fn=replace_face,
    inputs=[
        gr.Image(type="pil", label="Upload Person Image"),
        gr.Slider(0, 500, 70, step=1, label="Face X Coordinate"),
        gr.Slider(0, 500, 40, step=1, label="Face Y Coordinate"),
        gr.Slider(10, 200, 100, step=1, label="Face Width"),
        gr.Slider(10, 200, 100, step=1, label="Face Height"),
    ],
    outputs=gr.Image(type="pil", label="Result Image"),
    allow_flagging="never",
    title="Chill Guy Maker!",
    description="Upload your image, adjust the face coordinates, and become a chill guy."
)

interface.launch()
