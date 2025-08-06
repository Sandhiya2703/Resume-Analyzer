# 📄 Resume Analyzer – AI-Based Resume Matcher

A smart and interactive web application that helps **match resumes with job descriptions** using AI-powered keyword extraction and similarity scoring. Built using **Python**, **Streamlit**, **spaCy**, and **PyPDF2**.

---

## 🚀 Key Features

- 📤 Upload **Resume** and **Job Description** in PDF format
- 🔍 Extracts and cleans text using **PyPDF2** and **spaCy**
- ✅ Calculates a **matching score** between resume and job description
- 📊 Displays results in a clean and user-friendly Streamlit interface
- 💡 Helps recruiters and candidates save time in screening

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**: PyPDF2, spaCy, Scikit-learn, NumPy
- **NLP**: spaCy for keyword extraction and text processing

---

## 🧠 How It Works

1. **User uploads**:
   - Resume (PDF)
   - Job Description (PDF)

2. **Text Extraction**:
   - PyPDF2 extracts raw text from both files

3. **Keyword Extraction**:
   - spaCy processes and extracts relevant technical terms, skills, and keywords

4. **Matching Score**:
   - A simple NLP-based similarity algorithm calculates how well the resume matches the job

5. **Result**:
   - A match percentage is displayed on the screen

---

## 🖥️ Screenshots

![App Screenshot](images/screenshot.png)

---

## 📦 Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
Create virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run app.py
📁 Project Structure
bash
Copy
Edit
resume-analyzer/
│
├── app.py                  # Main Streamlit app
├── utils.py                # Helper functions for processing
├── model/                  # (Optional) Saved models
├── uploads/                # Uploaded PDFs
├── requirements.txt        # Project dependencies
├── README.md               # This file
└── images/                 # Screenshots and visuals
📌 Future Add-ons
🔍 Add job-role-specific scoring (Data Scientist, Web Developer, etc.)

🧠 Integrate ML/NLP-based ranking algorithms

🗂 Export analyzed data as a report

📧 Email result to user

👩‍💻 Author
Made with ❤️ by Sandhiya
🔗 LinkedIn

Sample output:

<img width="918" height="873" alt="Screenshot 2025-06-26 222853" src="https://github.com/user-attachments/assets/a681d5db-04fc-4340-b303-6b527459fe9c" />
<img width="985" height="801" alt="Screenshot 2025-06-26 222928" src="https://github.com/user-attachments/assets/4dc7d6c6-20ce-47ca-b7ae-88265dd35214" />
<img width="901" height="860" alt="Screenshot 2025-06-26 222908" src="https://github.com/user-attachments/assets/a904cf77-c00e-47a6-95ec-79dfc6d51c52" />





📜 License
This project is open-source and free to use for educational purposes. Licensed under the MIT License.

⭐ Support This Project
If you found this project useful:

🌟 Star this repository

🤝 Follow me on LinkedIn

🗣 Share with friends or recruiters

Thanks for your support! 💫











