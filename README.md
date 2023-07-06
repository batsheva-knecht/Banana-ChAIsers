# Banana ChAIser 🍌🚗

Banana ChAIser is an object-detective-driven car project developed as part of Hailo MAD Hacks 2023. This project combines the power of Hailo's hardware accelerators with the YOLOv5 network, gstreamer, and post-processing detection to create an engaging and interactive experience.

## Overview 📜

The main objective of Banana ChAIser is to showcase the capabilities of Hailo's technology in the context of object detection and tracking. In this project, we simulate a real-life scenario where a vehicle chases a target object, specifically a banana 🍌. The banana acts as a simulated gun 🔫, and the car is programmed to identify and track the banana holder using the YOLOv5 network. This demonstration not only highlights the power of object detection but also demonstrates Hailo's hardware accelerators in delivering fast and efficient inference for real-time applications.

## Technologies Used 🛠️

- **YOLOv5**: The project utilizes the YOLOv5 object detection model, renowned for its accuracy and efficiency in real-time detection tasks.
- **GStreamer**: GStreamer, an open-source multimedia framework, is employed for handling multimedia data in the project. It enables smooth streaming and processing of video data, crucial for real-time object detection.
- **Hailo**: Hailo's hardware accelerators play a vital role in this project, showcasing their capabilities for accelerating AI workloads. Hailo's hardware accelerators enhance the overall performance of Banana ChAIser, enabling fast and efficient inference for the YOLOv5 model.

## Installation and Setup 🚀

To run Banana ChAIser on your local machine, follow these steps:

1. Obtain the Hailo Tappas container v3.23.0.
2. Clone the Banana ChAIser repository from GitHub (https://github.com/batsheva-knecht/Banana-ChAIsers).
3. Install the necessary dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
4. Download the YOLOv5 model weights and place them in the designated directory.
5. Set up the Hailo hardware accelerator according to the instructions provided by Hailo.
6. Connect the necessary peripherals (camera, car controller, etc.) to your system.

## Usage 🚦

1. Open a terminal and navigate to the Banana ChAIser project directory.
2. Start the Hailo Tappas container v3.23.0 by running the command:
   ```
   docker run --privileged -it hailoai/tappas:3.23.0
   ```
3. Inside the container, execute the main script using the following command:
   ```
   ./multi_stream_detection.sh
   ```
4. Banana ChAIser will initialize and start detecting objects in the camera feed.
5. Hold the banana (acting as a gun) in front of the camera to initiate the car chasing sequence.
6. Observe how Banana ChAIser tracks and follows the banana holder.

## Customization 🧩

Banana ChAIser can be customized and extended in several ways:

- **Target Object**: The object detection model can be trained on other objects of interest. By collecting a dataset and retraining the YOLOv5 model, you can make Banana ChAIser chase different objects.
- **Car Control**: The behavior of the car, such as acceleration, turning, and stopping, can be customized to suit specific requirements.
- **Additional Features**: You can incorporate additional features into Banana ChAIser, such as obstacle avoidance or path planning, to enhance its functionality and make it more autonomous.


## Contributors 👥

Banana ChAIser is a project developed as part of Hailo MAD Hacks 2023. We would like to acknowledge the following contributors:

- Eran Gur: Project Lead
- Batsheva Knecht
- Dan Hanegbi
- Yasmine Hallel
- Ronit Shpoliansky
- Aviv Harel

We appreciate the efforts and contributions of all team members in bringing Banana ChAIser to life during Hailo MAD Hacks 2023.

## Conclusion 🎉

Banana ChAIser, developed as part of Hailo MAD Hacks 2023, showcases the fusion of object detection, tracking algorithms, and Hailo's hardware accelerators. By simulating a chase scenario with a banana acting as a gun, this project demonstrates the capabilities of the YOLOv5 network and Hailo's hardware accelerators. We hope Banana ChAIser inspires further exploration in the field of computer vision and autonomous systems.