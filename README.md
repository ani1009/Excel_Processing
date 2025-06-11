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


### Project Insights:
 Potential Improvements -
1. Support for Other Excel Formats: Right now, the app only reads .xls files. We can enhance it to support .xlsx, .csv, or even Google Sheets by using libraries like openpyxl, csv, or gspread.
2. File Upload Feature: Instead of hardcoding the file path, users could upload their own Excel files through an API endpoint. This would make the app more flexible and user-friendly.
3. Better Error Messages: The app can give more helpful and specific error messages, like “Table not found” or “Row not found” instead of generic 404s


### Testing: -
 I tested the API using both Swagger UI and Postman.
 All three endpoints (/list_tables, /get_table_details, and /row_sum) worked correctly after giving valid table and row names.
 I also tried different values for the occurrence parameter and tested cases where the table or row didn’t exist to confirm that errors were handled properly.
