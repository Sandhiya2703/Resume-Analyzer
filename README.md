# 😊 Face Emotion Detection using CNN & OpenCV

This project is a deep learning-based **Face Emotion Detection** system built using **Convolutional Neural Networks (CNN)** and **OpenCV**. It detects real-time facial emotions such as Happy, Sad, Angry, Surprise, Neutral, etc., using your webcam.

---

## 📌 Features

- Detects human faces in real-time via webcam.
- Classifies facial emotions (e.g., Happy, Sad, Angry, Surprise, Neutral).
- Built with Python, OpenCV, TensorFlow/Keras.
- Lightweight and works on CPU.
- Easy-to-use interface with live webcam feed.

---

## 🛠️ Technologies Used

- Python 🐍
- OpenCV 🎥
- TensorFlow / Keras 🧠
- NumPy 📊
- Pre-trained Haar Cascade for face detection

---

## 🚀 How It Works

1. The webcam feed is captured using OpenCV.
2. The face is detected using Haar Cascade classifier.
3. The face ROI is preprocessed (resized, grayscaled).
4. A trained CNN model predicts the emotion.
5. The emotion is displayed on the video feed in real-time.

---

## 🔧 Installation Steps

1. **Clone the repository**


git clone https://github.com/your-username/face-emotion-detector.git
cd face-emotion-detector
Install dependencies

Make sure Python 3 is installed. Then run:


pip install -r requirements.txt
Run the application


python main.py
🧠 Model Training (Optional)
If you want to retrain the model:

Use FER2013 or any labeled emotion dataset.

Train a CNN with emotion labels.

Save the model as model.h5.

📂 Project Structure
face-emotion-detector/
│
├── main.py                 # Main app with webcam feed
├── model.h5                # Trained CNN model
├── haarcascade_frontalface_default.xml
├── requirements.txt        # Python libraries
└── README.md               # This file
📸 Sample Output

🔒 Future Add-ons
🔊 Voice alert when Angry/Sad detected

🧓 Age & Gender Detection

📈 Logging emotion data for analysis

🙋‍♀️ Author
Made with ❤️ by Sandhiya



📄 License
This project is open-source and free to use for educational purposes.


## ⭐ Support This Project

If you liked this project:

- 🌟 **Star this repository** on GitHub
- 🤝 **Follow me on [LinkedIn](https://www.linkedin.com/in/sandhiya-v-it-461a262b2?)** for more projects and updates
- 🗣️ Feel free to connect or reach out for collaboration!

Thanks for your support! ❤️











