# 📦 ParcelSort & Barcode Generator

This repository contains two projects:
1. **ParcelSort** - A Django-based barcode reader and parcel sorting system.
2. **Barcode Generator** - A Python-based barcode generation tool.

---

## 📂 Project Structure

### ParcelSort
```
ParcelSort_Project/
│── barcodes/               # Stores scanned barcode images
│── barcode_scanner/        # Django app for barcode scanning
│── parcelsort/             # Main Django project directory
│── venv/                   # Virtual environment
│── .gitattributes          # Git attribute rules
│── .gitignore              # Ignored files for Git
│── manage.py               # Django management script
│── requirements.txt        # Project dependencies
```

### Barcode Generator
```
Bar_Code_Generator/
│── barcode_generator.py    # Python script to generate barcodes
│── requirements.txt        # Dependencies for barcode generation
│── .gitignore              # Git ignore rules
│── venv/                   # Virtual environment
│── generated_barcodes/     # Folder to store generated barcodes
```

---

## 🚀 Features

### ParcelSort
- 📸 **Barcode Scanning**: Upload and process barcode images.
- 📂 **Efficient Parcel Sorting**: Automates package classification.
- 🛠 **Django-Powered**: Built with Django for scalability.
- 💾 **Database Integration**: Stores barcode data for tracking.

### Barcode Generator
- 🔢 **Generate Barcodes**: Supports Code128, EAN-13, and EAN-8 formats.
- 🖼 **Saves as Image**: Generates and saves barcodes as PNG files.
- 💡 **Standalone or Integrated Use**: Can be used independently or with ParcelSort.

---

## ⚡ Installation

### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-username/ParcelSort_Project.git
cd ParcelSort_Project
```

### 2️⃣ Create and activate a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```sh
python manage.py migrate
```

### 5️⃣ Run the Django development server
```sh
python manage.py runserver
```

📌 **Usage**
- Navigate to `http://127.0.0.1:8000/`
- Upload a barcode image
- View the scanned data on the result page

---

## 🔢 Using the Barcode Generator

### 1️⃣ Clone the Barcode Generator repository
```sh
git clone https://github.com/Vimal-Babu/Bar_Code_Generator.git
cd Bar_Code_Generator
```

### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the barcode generator script
```sh
python barcode_generator.py
```

- Choose the barcode format (Code128, EAN-13, EAN-8).
- Enter the required data.
- The barcode image will be saved in the project folder.

---

## 📜 License
This project is open-source and available under the MIT License.

