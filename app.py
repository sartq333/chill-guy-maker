import gradio as gr
from face_parsing import integration_with_meme

def replace_face(person_image, face_x, face_y, face_width, face_height, flip):
    result_image = integration_with_meme(input_img_path=person_image, face_x=face_x, face_y=face_y, face_width=face_width, face_height=face_height, flip=flip)
    return result_image

interface = gr.Interface(
    fn=replace_face,
    inputs=[
        gr.Image(type="pil", label="Upload Person Image"),
        gr.Slider(0, 500, 70, step=1, label="Face X Coordinate"),
        gr.Slider(0, 500, 40, step=1, label="Face Y Coordinate"),
        gr.Slider(10, 200, 100, step=1, label="Face Width"),
        gr.Slider(10, 200, 100, step=1, label="Face Height"),
        gr.Checkbox(label="Flip Person Image Horizontally"),
    ],
    outputs=gr.Image(type="pil", label="Result Image"),
    allow_flagging="never",
    title="Chill Guy Maker!",
    description="Upload your image, adjust the face coordinates, and become a chill guy. Upload your image, adjust the face coordinates, and become a chill guy. Check the project readme for more information: https://github.com/sartq333/chill-guy-maker/blob/main/README.md"
)

interface.launch()
