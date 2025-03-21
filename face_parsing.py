import numpy as np
import json
import torch
from transformers import SegformerImageProcessor, SegformerForSemanticSegmentation
from PIL import Image
from PIL import ImageOps
import matplotlib.pyplot as plt

def segmentation(input_img_path):
    with open('face-parsing/config.json', 'r') as file:
        data = json.load(file)

    for key, value in data["id2label"].items():
        print(f"{key}: {value}")

    image_processor = SegformerImageProcessor.from_pretrained("face-parsing")
    model = SegformerForSemanticSegmentation.from_pretrained("face-parsing")

    # input_img_path = "akshay kumar img.jpeg"
    if isinstance(input_img_path, str):  # It's a path
        image = Image.open(input_img_path)
    else:  # It's already an image object
        image = input_img_path
        
    image = image.convert("RGB")

    # new_size = (128, 128)
    # image = image.resize(new_size)
    # plt.imshow(image)
    # plt.axis("off")
    # plt.show()

    inputs = image_processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    color_map = np.array([
        [255, 255, 255],  # 0 background
        [255, 0, 0],      # 1 skin
        [0, 255, 0],      # 2 nose
        [0, 0, 255],      # 3 eye_g
        [255, 255, 0],    # 4 l_eye
        [255, 0, 255],    # 5 r_eye
        [0, 255, 255],    # 6 l_brow
        [192, 192, 192],  # 7 r_brow
        [128, 128, 128],  # 8 l_ear
        [128, 0, 0],      # 9 r_ear
        [128, 128, 0],    # 10 mouth
        [0, 128, 0],      # 11 u_lip
        [0, 128, 128],    # 12 l_lip
        [0, 0, 128],      # 13 hair
        [255, 165, 0],    # 14 hat
        [75, 0, 130],     # 15 ear_r
        [240, 230, 140],  # 16 neck_l
        [255, 20, 147],   # 17 neck
        [100, 149, 237]   # 18 cloth
    ])

    predicted_classes = torch.argmax(outputs["logits"], dim=1).squeeze().cpu().numpy()
    segmentation_map = color_map[predicted_classes]

    outputs["logits"] = outputs["logits"].squeeze()
    outputs["logits"].shape

    img = np.array(image)
    print(img.shape)
    print(segmentation_map.shape)

    face_mask = outputs["logits"][1]
    print(face_mask)

    # plt.figure(figsize=(15, 7))
    # plt.subplot(1, 2, 1)
    # plt.title("Original Image")
    # plt.imshow(image)
    # plt.axis('off')

    # plt.subplot(1, 2, 2)
    # plt.title("Predicted Segmentation Map")
    # plt.imshow(segmentation_map)
    # plt.axis('off')

    # plt.show()

    new_size = (128, 128)
    image = image.resize(new_size)
    original_image_np = np.array(image)
    segmented_image_np = np.array(segmentation_map)

    skin_color = [255, 0, 0]
    eyeg_color = [0, 0, 255]
    nose_color = [0, 255, 0]
    leye_color = [255, 255, 0]
    reye_color = [255, 0, 255]
    lbrow_color = [0, 255, 255]
    rbrow_color = [192, 192, 192]
    lear_color = [128, 128, 128]
    rear_color = [128, 0, 0]
    mouth_color = [128, 128, 0]
    ulip_color = [0, 128, 0]
    llip_color = [0, 128, 128]
    hair_color = [0, 0, 128]
    hat_color = [255, 165, 0]
    neck_color = [255, 20, 147]

    skin_mask = np.all(segmented_image_np == skin_color, axis=-1)
    eyeg_mask = np.all(segmented_image_np == eyeg_color, axis=-1)
    nose_mask = np.all(segmented_image_np == nose_color, axis=-1)
    leye_mask = np.all(segmented_image_np == leye_color, axis=-1)
    reye_mask = np.all(segmented_image_np == reye_color, axis=-1)
    lbrow_mask = np.all(segmented_image_np == lbrow_color, axis=-1)
    rbrow_mask = np.all(segmented_image_np == rbrow_color, axis=-1)
    lear_mask = np.all(segmented_image_np == lear_color, axis=-1)
    rear_mask = np.all(segmented_image_np == rear_color, axis=-1)
    mouth_mask = np.all(segmented_image_np == mouth_color, axis=-1)
    ulip_mask = np.all(segmented_image_np == ulip_color, axis=-1)
    llip_mask = np.all(segmented_image_np == llip_color, axis=-1)
    hair_mask = np.all(segmented_image_np == hair_color, axis=-1)
    hat_mask = np.all(segmented_image_np == hat_color, axis=-1)
    neck_mask = np.all(segmented_image_np == neck_color, axis=-1)

    # combining all the masks
    combined_mask = np.logical_or.reduce((
        skin_mask, eyeg_mask, nose_mask, leye_mask, reye_mask,
        lbrow_mask, rbrow_mask, lear_mask, rear_mask,
        mouth_mask, ulip_mask, llip_mask, hair_mask,
        hat_mask, neck_mask
    ))

    # applying the combined mask to the original image
    selected_regions = np.full_like(original_image_np, 255)

    selected_regions[combined_mask] = original_image_np[combined_mask]

    # # Visualize the results
    # plt.figure(figsize=(15, 5))

    # # Display the original image
    # plt.subplot(1, 3, 1)
    # plt.imshow(image)
    # plt.title("Original Image")
    # plt.axis("off")

    # # Display the segmented image
    # plt.subplot(1, 3, 2)
    # plt.imshow(segmentation_map)
    # plt.title("Segmented Image")
    # plt.axis("off")

    # # Display the extracted regions
    # plt.subplot(1, 3, 3)
    # plt.imshow(Image.fromarray(selected_regions))
    # plt.title("Selected Regions")
    # plt.axis("off")

    # plt.tight_layout()
    # plt.show()

    selected_regions = Image.fromarray(selected_regions)
    # selected_regions.save("only_face.jpg")
    return selected_regions

"""challenges as of now:
1. meme face image is not eradicated (manually remove this). (done!)
2. note down the width of the neck of meme image and make adjustements accordingly so that the target face gets fixed on the meme image. (pending)
3. background in the person's image is black, which is messing up with hair, fix that.
"""

def integration_with_meme(input_img_path, face_x, face_y, face_width, face_height, flip):

    person_image = segmentation(input_img_path)
    # person_image = Image.open('only_face.jpg')
    meme_image = Image.open('chillguy.jpeg')

    # Convert meme image to RGBA (for transparency handling) and to a NumPy array
    meme_image = meme_image.convert("RGBA")
    meme_data = np.array(meme_image)

    # Define the coordinates of the face region in the meme image
    # face_x, face_y, face_width, face_height = 0, 40, 180, 110  # Adjust based on meme image

    # Clamp the face region to ensure it is within bounds
    meme_height, meme_width = meme_data.shape[:2]
    face_width = min(face_width, meme_width - face_x)
    face_height = min(face_height, meme_height - face_y)

    # Resize the person's image to fit the face region
    person_resized = person_image.resize((face_width, face_height)).convert("RGBA")

    if flip:
        person_resized = ImageOps.mirror(person_resized)
        
    person_data = np.array(person_resized)

    r, g, b, a = person_data[..., 0], person_data[..., 1], person_data[..., 2], person_data[..., 3]
    white_areas = (r > 230) & (g > 230) & (b > 230)
    person_data[white_areas, 3] = 0

    person_resized = Image.fromarray(person_data)

    face_region = meme_data[face_y:face_y+face_height, face_x:face_x+face_width]

    face_region_resized = Image.fromarray(face_region).resize((face_width, face_height))

    blended_region = Image.alpha_composite(face_region_resized, person_resized)

    blended_region_data = np.array(blended_region)
    meme_data[face_y:face_y+face_height, face_x:face_x+face_width] = blended_region_data

    result_image = Image.fromarray(meme_data)

    # plt.imshow(result_image)
    # plt.axis("off")
    # plt.show()

    meme_image = np.array(meme_image)
    print(meme_image.shape)
    result_image = np.array(result_image)
    print(result_image.shape)
    return result_image

# integration_with_meme(input_img_path="akshay kumar img.jpeg", face_x=0, face_y=40, face_width=180, face_height=110)
