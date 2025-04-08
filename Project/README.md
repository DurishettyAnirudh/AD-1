# 🎥 **AI Video Generator**

🚀 **AI Video Generator** automates the creation of high-quality videos by combining **script generation, TTS voiceovers, captions, and stock footage** into a single workflow. It utilizes **OpenAI** for script generation, **EdgeTTS** for voiceovers, **Whisper** for captions, and **MoviePy** for seamless video rendering.

---

## 🔥 **Features**

✅ **Automated Script Generation:** Uses ChatGPT  to create contextual scripts.\
✅ **Text-to-Speech (TTS) Voiceovers:** Realistic voice synthesis with EdgeTTS.\
✅ **Timed Captions:** Accurate captioning with Whisper AI.\
✅ **Stock Footage Retrieval:** Fetches free, high-quality videos from Pexels.\
✅ **Video Rendering:** Combines all elements into a polished MP4 video.\
✅ **Logging:** Tracks all GPT and Pexels API calls for auditing.

---

## ⚙️ **Tech Stack**

- **Python 3.11**
- **OpenAI GPT-4o / Groq LLaMA3** for script generation
- **EdgeTTS** for text-to-speech voiceovers
- **Pexels API** for stock video retrieval
- **Whisper** for captioning
- **MoviePy** for video rendering
- **JSON & Logging** for tracking API responses

---

## 📂 **Project Structure**

```
/Project  
 ├── app.py                      # Main entry point  
 ├── VideoMaker.py               # Orchestrator script  
 ├── requirements.txt            # Python dependencies  
 ├── README.md                   # Documentation  
 │  
 ├── 📂 .logs                     # Logs for API requests  
 │   ├── gpt_logs                 # Logs for GPT responses  
 │   └── pexel_logs               # Logs for Pexels queries  
 │  
 ├── 📂 utility                   # Core modules  
 │   ├── utils.py                  # Logging utilities  
 │  
 │   ├── 📂 audio                  # TTS voiceover module  
 │   │   └── audio_generator.py    # Generates TTS voice  
 │  
 │   ├── 📂 captions               # Captioning module  
 │   │   └── timed_captions_generator.py   # Generates captions with Whisper  
 │  
 │   ├── 📂 render                 # Video rendering module  
 │   │   └── render_engine.py      # Combines video, captions, and audio  
 │  
 │   ├── 📂 script                 # Script generation  
 │   │   └── script_generator.py   # GPT-based script generator  
 │  
 │   ├── 📂 video                  # Video search and selection  
 │   │   ├── background_video_generator.py  # Fetches stock videos  
 │   │   └── video_search_query_generator.py # Generates video search queries  
 │  
 └── rendered_video.mp4          # Output sample video  
```

---

## 🚀 **Installation**

### 🛠️ **1. Clone the Repository**

```bash
git clone <YOUR_REPO_URL>
cd ai-video-generator
```

### 📦 **2. Create a Virtual Environment**

```bash
python -m venv venv  
source venv/bin/activate   # On Linux/Mac  
venv\Scripts\activate      # On Windows  
```

### ⚙️ **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### 🔑 **4. Set Up Environment Variables**

Create a `Passwrds.py` file in the root directory with your **API keys**:

```
OPENAI_KEY=<YOUR_OPENAI_API_KEY>  
PEXELS_KEY=<YOUR_PEXELS_API_KEY>  
GROQ_API_KEY=<YOUR_GROQ_API_KEY>  # (optional)  
```

---

## ▶️ **Usage**

### 1️⃣ **Run the Main Script**

To create a video, simply run:

```bash
streamlit run VideoMaker.py
```

### 2️⃣ **Custom Execution**

Run individual modules:

```bash
# Script Generation
python utility/script/script_generator.py  

# TTS Voiceover
python utility/audio/audio_generator.py  

# Captioning
python utility/captions/timed_captions_generator.py  

# Video Rendering
python utility/render/render_engine.py  
```

---

## 🔥 **Example Execution**

1. The system generates a **script** based on the prompt.
2. It creates **TTS audio** with EdgeTTS.
3. Captions are generated with Whisper.
4. **Pexels API** retrieves stock footage.
5. The **MoviePy renderer** combines everything into a final video.
6. The video is saved in the `/Project` directory as `rendered_video.mp4`.

---

## 🛠️ **Troubleshooting**

✅ **Issue:** `ModuleNotFoundError: No module named 'dotenv'`\
💡 **Solution:** Install dotenv using:

```bash
pip install python-dotenv
```

✅ **Issue:** `PEXELS_KEY` or `OPENAI_KEY` not recognized\
💡 **Solution:** Double-check `.env` configuration and restart the terminal.

✅ **Issue:** Whisper model missing\
💡 **Solution:** Install Whisper with:

```bash
pip install whisper
```

---

## 🔥 **Customization Tips**

💡 **Change GPT Model:**\
In `script_generator.py`, modify the model:

```python
model = "gpt-4o"  # GPT-4o  
# OR  
model = "llama3-70b-8192"  # Groq LLaMA  
```

💡 **Adjust Voiceover Style:**\
Modify EdgeTTS parameters in `audio_generator.py`:

```python
rate='+10%'   # Faster speech  
volume='+5%'  # Louder voice  
```

💡 **Modify Video Duration:**\
In `background_video_generator.py`, change the duration:

```python
duration = 10  # Video length in seconds  
```

---

## 🔥 **API References**

- **OpenAI API:** [OpenAI](https://platform.openai.com/docs)
- **Pexels API:** [Pexels](https://www.pexels.com/api/)
- **Whisper Model:** [OpenAI Whisper](https://openai.com/whisper/)
- **MoviePy:** [MoviePy](https://zulko.github.io/moviepy/)

---

## 👥 **Contributors**

- **D. Anirudh** – *Project Lead* *API Integration*

---


