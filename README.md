# IntelliData Analyst  
### AI-Powered Autonomous Data Analyst With Multi-Agent Intelligence  
*(Built with LangChain, FastAPI, Streamlit, Pandas, Matplotlib & Gemini API)*

IntelliData Analyst is a fully automated, multi-agent system that uploads any CSV file and instantly performs:

✔ Data Cleaning  
✔ Exploratory Data Analysis (EDA)  
✔ Anomaly Detection  
✔ Automatic Visualizations  
✔ Natural-Language Q&A  

All powered by intelligent AI agents communicating through a FastAPI backend and Streamlit frontend.

---

#  Features

##  Automatic Data Cleaning Agent
- Handles missing values  
- Removes duplicates  
- Identifies inconsistent formats  
- Generates a **Data Quality Report**

---

## EDA Agent (Exploratory Data Analysis)
Produces in-depth insights including:

- Statistical summary  
- Column-level patterns  
- Correlation analysis  
- Categorical distribution  
- Outlier detection  

---

## Anomaly Detection Agent
Finds:

- Numerical outliers  
- Sudden spikes/drops  
- Irregular category patterns  

---

## Automatic Visualization Agent
Generates the right visuals automatically:

- Histograms  
- Bar Charts  
- Scatterplots  
- Boxplots  
- Line Charts  
- Heatmaps  

Charts are sent to Streamlit as **base64 images** and displayed instantly.

---

##  Natural-Language Q&A Agent
Ask questions such as:

- “What column has the highest variance?”  
- “Show the relationship between age and salary.”  
- “Summarize this dataset.”  
- “Explain the trend in monthly sales.”  

Uses **Gemini + RAG + EDA results** for precise answers.

---

##  Streamlit UI
Interactive dashboard where users can:

- Upload datasets  
- View statistics  
- Explore charts  
- Read anomaly reports  
- Ask questions about the dataset  

---

## FastAPI Backend
Handles:

- Multi-agent orchestration  
- Data cleaning  
- Visualization creation  
- Q&A  
- RAG storage  
- API endpoints  

---

# System Architecture

User  
↓  
Streamlit Frontend  
↓  
FastAPI Backend  
↓  
AI Multi-Agent Coordinator  
↓  
├── Cleaning Agent  
├── EDA Agent  
├── Anomaly Agent  
├── Visualization Agent  
└── Q&A Agent  
↓  
Pandas / Matplotlib / Gemini API  
↓  
Final Response to User  

---

# Project Structure

INTELLIDATA_ANALYST  
├── app/  
│   ├── agents/  
│   │   ├── analysis_agent.py  
│   │   ├── cleaning_agent.py  
│   │   ├── visualization_agent.py  
│   │   ├── chat_agent.py  
│   │   └── coordinator.py  
│   ├── database/  
│   │   └── vector_db.py  
│   ├── models/  
│   │   └── schemas.py  
│   └── utils/  
│       └── gemini_client.py  
│  
├── uploads/  
├── chroma_db/  
├── main.py  
├── frontend.py  
├── requirements.txt  
├── Dockerfile  
└── .env  

---

# Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/IntelliData-Analyst.git
cd IntelliData-Analyst
```

### 2. Add your environment variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

### Start FastAPI Backend

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Start Streamlit Frontend

```bash
streamlit run frontend.py
```

## Docker Support

### Build Docker Image:

```
docker pull snehaghoshnew2003/intellidata-analyst:latest
```

### Run Full System:

```
docker run -p 8000:8000 -p 8501:8501 snehaghoshnew2003/intellidata-analyst:latest
```
This will automatically start:

Backend → **http://localhost:8000**  
Frontend → **http://localhost:8501** 

## Example Questions

“What are the top insights from this dataset?”
“Which features correlate the most?”
“List anomalies in each numerical column.”
“Tell me the distribution of categories.”

## Tech Stack

### AI & Agents  
- Gemini API  
- LangChain  
- RAG + Vector DB  

### Backend  
- FastAPI  
- Pydantic  
- ChromaDB  

### Data Processing  
- Pandas  
- Matplotlib  
- Seaborn  

### Frontend  
- Streamlit  
- Base64 Image Rendering  

## Why IntelliData Analyst is Resume-Ready

- Fully autonomous multi-agent pipeline  
- Clean modular architecture  
- Real-world Data Analyst workflow  
- Automatic chart generation  
- Natural-language insights  
- Production-ready Docker setup  

## Future Enhancements

- Auto-generated PDF reports  
- SQL integration  
- Dashboard export  
- Advanced ML forecasting  
- Deep anomaly detection  
- Multi-file comparative analysis  

## Contact

If you want help with deployment, feel free to reach out anytime!
