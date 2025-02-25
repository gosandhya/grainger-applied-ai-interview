# Grainger Applied AI Interview

This repository contains a project for the Grainger Applied AI interview process. It includes scripts for generating a dataset, processing it, and storing prompts used in the workflow.

## Project Structure

- `data.py` - processes and generates the dataset according to assignment specification.
- `main.py` - Processes the dataset and generates desired output.
- `prompt_store.py` - Stores the prompt used in the workflow.

## How to Run

Follow these steps to run the project in the correct order:

### 1. Clone the Repository
```bash
git clone https://github.com/gosandhya/grainger-applied-ai-interview.git
cd grainger-applied-ai-interview
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  
```

### 3. Install Dependencies
Ensure you have the required dependencies installed:
```bash
pip install -r requirements.txt  # If a requirements file exists
```

### 4. Generate the Dataset
Run the `data.py` script to create the dataset:
```bash
python data.py
```

### 5. Run the Main Processing Script
Use `main.py` to process the dataset and generate output:
```bash
python main.py
```

### 6. Utilize the Prompt Store
The `prompt_store.py` contains stored prompts used in the project. You can modify or extend them as needed.

## Notes
- Ensure you have Python installed (preferably 3.8 or later).
- If any additional dependencies are required, add them to `requirements.txt`.

## License
This project is for interview purposes and does not have a specified license.


