# 🏫 FreeClass Finder – Django Web App

**FreeClass Finder** is a Django-based web application that helps students and faculty members quickly find **unoccupied classrooms** across different blocks and floors of a college during specific time slots.

---

## 🚀 Features Implemented

- 🔍 **Search by Block, Floor, Day, and Time**
- ✅ **Filter Results**
  - All Rooms
  - Available Rooms
  - Occupied Rooms
- 🗃️ **Room Sorting** by Room Number
- 📋 Dynamic dropdowns powered by database data
- 🧠 Clean, user-friendly UI for ease of use


## 🛠️ Tech Stack

| Technology  | Description                      |
|-------------|----------------------------------|
| Django      | Python web framework (backend)   |
| HTML/CSS    | Frontend templating              |
| SQLite3     | Default Django DB (development)  |
| Bootstrap   | UI Styling (optional)            |



## ⚙️ How It Works

1. User selects a Block, Floor, Day, and Time.
2. App queries the database model `FreeClass` to find rooms matching those filters.
3. Results are shown:
   - 🟩 **Available**: Rooms that are **not occupied**
   - 🟥 **Occupied**: Rooms that are **currently in use**
   - 🟨 **All**: Both available and occupied rooms


👤 Author
Nadhil – Portfolio Website
GitHub: https://github.com/Nadhil-an/
