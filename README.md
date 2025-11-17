# Globussoft_Assessment
# Globussoft_Assessment
Python Projects Collection

This repository contains two separate Python projects:

**Task 1 – Amazon Laptop Scraper**

**Task 2 – Face Authentication (FastAPI Service)**

Each project has its own folder, dependencies, and instructions.

**Task 1 – Amazon Laptop Scraper**

This Python script scrapes laptop product details from Amazon.in and saves them in a CSV file.

*What it Does*

The scraper collects the following information for each laptop:

Image - Product image URL

Title - Name of the laptop

Rating - Customer rating

Price - Current price in INR

Ad / Organic - Whether the product is a sponsored ad or organic listing

*How to Run*

Make sure you have Python 3.x installed.

Install the required packages:

pip install -r requirements.txt


*Run the script:*

python amazon_scraper.py


A CSV file will be generated automatically with a timestamped filename.

Folder Structure
Task1/
├─ amazon_scraper.py        # Python script for scraping laptops
├─ amazon_laptops_20251117_064142.csv  # Sample CSV output
├─ requirements.txt         # Python dependencies
├─ Sample_Output          # Sample Output images
└─ README.md            # Instructions

**Task 2 – Face Authentication (FastAPI Service)**

This project is a Python-based Face Authentication API that can verify whether two face images belong to the same person. It uses deep learning embeddings to compare faces.

*Features*

Accepts two face images as input.

Detects faces in both images.

Computes similarity and returns:

Verification result: Same or Different person

Similarity score

Bounding boxes of detected faces

*How to Run*

Make sure you have Python 3.x installed.

Install all required packages:

pip install -r requirements.txt


Start the FastAPI server:

cd Task2
uvicorn app:app --reload


Open your browser at:

http://127.0.0.1:8000/docs


You can test the API using the interactive Swagger interface.

Folder Structure
Task2/
├─ app.py               # FastAPI service code
├─ test_images/         # Sample images for testing
│  ├─ person1_1.jpg
│  ├─ person1_2.jpg
│  ├─ person2_1.jpg
│  └─ person2_2.jpg
├─ requirements.txt     # Python dependencies
├─ Sample_Output        # Sample Output images
└─ README.md            # Instructions
