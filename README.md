# ☁️ Cloud Oriented Web Applications (COWA)

**COWA** is a foundation for developing **cloud-based web applications**, built with **Python** and designed to interact seamlessly with **MongoDB**. It includes various modules for database operations, making it easy to manage data efficiently.

## 📌 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributors](#contributors)
- [License](#license)

## 🛠 Installation

Follow these steps to set up the project:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/bugra-university/cowa.git
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure MongoDB:**
   - Set up your MongoDB database.
   - Update the connection details in `mongo_connect.py`.

## 🚀 Usage

COWA includes the following modules for MongoDB interaction:

- **`mongo_connect.py`**: Establishes a connection to MongoDB.
- **`mongo_create.py`**: Inserts new documents into the database.
- **`mongo_read.py`**: Fetches and displays documents from the database.
- **`mongo_update.py`**: Updates existing documents.
- **`mongo_delete.py`**: Deletes specific documents.

Each module is designed for a specific function. Refer to the corresponding file for usage examples.

## 📂 File Structure

- `mongo_connect.py` → MongoDB connection handler
- `mongo_create.py` → Insert new documents
- `mongo_read.py` → Retrieve documents
- `mongo_update.py` → Update database entries
- `mongo_delete.py` → Delete documents
- `package.json` → Project dependencies
- `package-lock.json` → Dependency versions

## 👨‍💻 Contributors

- **Ramesh Dharavath**

We welcome contributions! Feel free to submit pull requests to improve the project.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

🚀 **Start building your cloud-based applications with COWA today!**

