from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from CSV
STUDENT_DATA_FILE = "q-vercel-python.json"

def load_marks():
    marks_dict = {}
    with open(STUDENT_DATA_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            marks_dict[row["name"]] = int(row["marks"])
    return marks_dict

marks_data = load_marks()

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    """
    Fetch marks for the requested student names.
    """
    result = [marks_data.get(n, None) for n in name]  # Preserve order
    return {"marks": result}
