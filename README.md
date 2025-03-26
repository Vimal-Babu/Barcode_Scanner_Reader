# 📦 ParcelSort Project

ParcelSort is a Django-based project designed to efficiently scan and process barcodes for parcel sorting. It includes a dedicated barcode scanning module.

## 🏗 Project Structure

ParcelSort_Project/ │── barcodes/ # Stores scanned barcode images │── barcode_scanner/ # Django app for barcode scanning │── parcelsort/ # Main Django project directory │── venv/ # Virtual environment │── .gitattributes # Git attribute rules │── .gitignore # Ignored files for Git │── manage.py # Django management script │── requirements.txt # Project dependencies

## 🚀 Features

- 📸 **Barcode Scanning**: Upload and process barcode images.
- 📂 **Efficient Parcel Sorting**: Automates package classification.
- 🛠 **Django-Powered**: Built with Django for scalability.
- 💾 **Database Integration**: Stores barcode data for tracking.

## ⚡ Installation

1️⃣ **Clone the repository**  
```sh
git clone https://github.com/your-username/ParcelSort_Project.git
cd ParcelSort_Project

2️⃣ Create and activate a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3️⃣ Install dependencies
```sh
pip install -r requrement.txt

4️⃣ Apply migrations
```sh
python manage.py migrate

5️⃣ Run the Django development server
```sh
python manage.py runserver


🖼 Barcode Upload and Scan
Navigate to http://127.0.0.1:8000/

Upload a barcode image.

View the scanned data on the result page.

📜 License
This project is open-source and available under the MIT License.


