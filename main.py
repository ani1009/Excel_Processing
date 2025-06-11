from fastapi import FastAPI, Query, HTTPException
from excel_utils import ExcelProcessor

app = FastAPI()

EXCEL_PATH = "Data/capbudg.xls"

@app.get("/list_tables")
def list_tables():
    processor = ExcelProcessor(EXCEL_PATH)
    return {"tables": processor.get_table_names()}

@app.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    processor = ExcelProcessor(EXCEL_PATH)
    try:
        rows = processor.get_table_rows(table_name)
        return {"table_name": table_name, "row_names": rows}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...), occurrence: int = Query(1)):
    processor = ExcelProcessor(EXCEL_PATH)
    try:
        total = processor.get_row_sum(table_name, row_name, occurrence)
        return {
            "table_name": table_name,
            "row_name": row_name,
            "occurrence": occurrence,
            "sum": total
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
