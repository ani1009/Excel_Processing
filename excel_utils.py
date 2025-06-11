import pandas as pd

class ExcelProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sheets = pd.read_excel(file_path, sheet_name=None, header=None)

    def get_table_names(self):
        return list(self.sheets.keys())

    def get_table_rows(self, table_name: str):
        if table_name not in self.sheets:
            raise ValueError(f"Table '{table_name}' not found.")
        df = self.sheets[table_name].dropna(how="all")
        return df.iloc[:, 0].dropna().astype(str).tolist()

    def get_row_sum(self, table_name: str, row_name: str, occurrence: int = 1) -> float:
        if table_name not in self.sheets:
            raise ValueError(f"Table '{table_name}' not found.")
        df = self.sheets[table_name].dropna(how="all")
        
        # Match rows based on first column
        matches = df[df.iloc[:, 0].astype(str).str.strip() == row_name.strip()]
        if matches.empty or len(matches) < occurrence:
            raise ValueError(f"'{row_name}' with occurrence {occurrence} not found in '{table_name}'.")

        # Pick the specific occurrence (1-indexed)
        selected_row = matches.iloc[occurrence - 1]
        
        # Try summing up numeric values from rest of row
        numeric_values = pd.to_numeric(selected_row.iloc[1:], errors='coerce')
        return numeric_values.dropna().sum()
