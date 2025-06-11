#  FastAPI Excel Processor

##  Overview
This FastAPI app reads and processes an Excel file (`/Data/capbudg.xls`) and exposes RESTful APIs to interact with its data.

##  How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt

### 2. Run the app
uvicorn main:app --reload --port 9090

## 3. To View
http://127.0.0.1:9090/docs