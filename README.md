# 🛡️ Safe Virus Study

A controlled and ethical simulation of a file-modifying, self-replicating virus developed as a part of an **Information Security final year project**. This Python-based script mimics the behavior of basic malware to demonstrate how it spreads, modifies files, and replicates — all within a **safe, isolated environment** without harming the actual system.

---

## 📌 Project Overview

This project is **NOT harmful** and is intended strictly for **educational purposes**. It allows you to:
- Simulate the delivery of malware via a **dummy phishing email**
- Observe how a virus can replicate itself and alter files
- Study the **limitations and controls** placed to ensure ethical usage

---

## 🧪 How It Works

1. **Phishing Simulation**:  
   A dummy phishing email is created, disguised as a free software installer. When executed, it triggers the virus simulation script.

2. **Targeted Folder Attack**:  
   The virus script automatically locates or creates a folder named `safe_virus_study` on the Desktop using this path:
   ```
   C:/Users/<Username>/Desktop/safe_virus_study
   ```

3. **File Modification**:  
   All `.txt` files in the target folder are **safely modified** by appending a harmless line:
   ```
   This file has been safely modified by a benign script.
   ```

4. **Self-Replication**:  
   The script creates **3 replicas** of itself in the same folder:
   - `replica_1.py`
   - `replica_2.py`
   - `replica_3.py`

5. **Controlled Spread**:  
   To prevent uncontrolled spreading:
   - Replicas **only replicate** if they are renamed manually.
   - A `.replicated` flag is generated to avoid recursive replication.

---

## 💻 Technologies Used

- **Python 3**
- Modules: `os`, `shutil`, `sys`
- Tested on Windows

---

## 📂 Project Structure

```
📁 safe_virus_study
├── original_script.py
├── replica_1.py
├── replica_2.py
├── replica_3.py
├── sample_file_1.txt
├── sample_file_2.txt
├── demo_video.mp4
```

---

## 🔒 Safety First

- The script does **not access system files** outside the specified folder.
- Only `.txt` files in the `safe_virus_study` folder are affected.
- Replication logic is strictly limited and controlled.
- No harmful payload is delivered — this is purely for safe research.

---

## 🎥 Demo

📽️ Watch the complete working demo on LinkedIn: [LinkedIn Project Post](https://www.linkedin.com/in/your-link-here)  
You can also find the video file in this repository.

---

## 📎 How to Use

1. Clone the repository or download the files.
2. Place some `.txt` files in the `safe_virus_study` folder on your Desktop.
3. Run `original_script.py`.
4. Observe file changes and replica creation.
5. Try renaming replicas to see replication in action.

---

## ⚠️ Disclaimer

This project is designed for **academic and demonstration purposes only**.  
Please do not use this script in any unethical or unauthorized manner.

---

## 📬 Contact

**Muhammad Wahaj Bin Aamir**  
Email: [wahajaamir2@gmail.com](mailto:wahajaamir2@gmail.com)  
LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

---

## ⭐ Give this repo a star if you found it interesting or helpful!
