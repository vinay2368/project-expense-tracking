
# 💰 Project Expense Tracking

A simple and efficient **Expense Tracking API** built using **FastAPI** that helps users manage and analyze their daily expenses.

---

## 🚀 Features

* Add new expenses
* Categorize expenses (Food, Travel, Bills, etc.)
* Add notes for each expense
* Fetch expenses by date range
* Analytics support for better financial insights

---

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **SQLite / Database (as used in your project)**

---

## 📂 Project Structure

```
project-expense-tracking/
│── main.py
│── db_helper.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/vinay2368/project-expense-tracking.git
cd project-expense-tracking
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
uvicorn main:app --reload
```

---

## 📡 API Endpoints

### ➤ Add Expense

```
POST /expenses
```

### ➤ Get Expenses by Date Range

```
POST /expenses/date-range
```

---

## 📊 Example Request

```json
{
  "amount": 500,
  "category": "Food",
  "notes": "Dinner"
}
```

---

## 🧠 Future Improvements

* Add user authentication
* Build frontend UI
* Add charts and analytics dashboard
* Deploy on cloud (AWS / Render / Railway)

---

## 🤝 Contributing

Feel free to fork this repo and contribute!

---

## 📌 Author

**Vinay Chaudhary**
GitHub: https://github.com/vinay2368

---

⭐ If you like this project, don't forget to give it a star!
