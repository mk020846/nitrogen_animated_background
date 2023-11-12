import cv2
import os
while True:
    file = "bg.gif"
    cap = cv2.VideoCapture(file)

    if not cap.isOpened():
        print("ERROR OPENING GIF")
        exit()

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    output_dir = "temp_frames"
    os.makedirs(output_dir, exist_ok=True)

    for frame_number in range(total_frames):
        ret,frame = cap.read()
        if not ret:
            break

        temp_image_path = os.path.join(output_dir,f"frame_{frame_number:04d}.png")
        cv2.imwrite(temp_image_path,frame)
        os.system(f"nitrogen --set-zoom-fill --save { temp_image_path }")

    cap.release()
