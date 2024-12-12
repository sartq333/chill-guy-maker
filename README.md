# chill-guy-maker

A fun project that lets you replace the face in a meme with another face using Python and Gradio.

Try out here: https://huggingface.co/spaces/Sartc/chillGuy_maker.
As of now, you'll have to adjust the face_x, face_y, face_width and face_height parameters to get the desired results, but I'll try to automate them too in future. 

![image](https://github.com/user-attachments/assets/638ce7ed-3829-43c4-8195-e5d0666bfadc)

![image](https://github.com/user-attachments/assets/0e69ab8a-06a2-4620-8112-efe8e7c3a507)


![image](https://github.com/user-attachments/assets/4cacd0c2-ee81-4f5e-b6e0-74301958b1f6)

![image](https://github.com/user-attachments/assets/21115774-4735-4583-ae4f-779d6c66a205)



---

## Features

- Replace faces in the chill guy meme with a custom face.
- Control the face's position, size, and orientation (optional flip). I will also try to automate this thing so that we can get final output without any intervention.

---

## How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/sartq333/meme-face-replacer.git
   cd meme-face-replacer
   ```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Launch the Gradio app:
```bash
    python3 app.py
```

Acknowledgments:

   Segmentation model used in this project has been taken from here: https://huggingface.co/jonathandinu/face-parsing.

   Built with Gradio and PyTorch.
   
   Inspired by dingboard.
