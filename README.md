# chill-guy-maker

A fun project that lets you replace the face in a meme with another face using Python and Gradio. This project supports flipping the input image horizontally, precise control over face placement, and background transparency handling.

![This is how final output looks like:](https://github.com/user-attachments/assets/638ce7ed-3829-43c4-8195-e5d0666bfadc)

![SS from hugging face spaces:](https://github.com/user-attachments/assets/f026c195-f951-4bb0-af11-f5fcbdafcb91)


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

    Install the dependencies:

pip install -r requirements.txt

Launch the Gradio app:

    python3 app.py

    Open the URL shown in your terminal to use the app.


Acknowledgments
    Segmentation model used in this project has been taken from here: https://huggingface.co/jonathandinu/face-parsing.
    Built with Gradio and PyTorch.
    Inspired by dingboard.
