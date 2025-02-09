# 🌍 Wikipedia Edits Analysis 📊


## 🚀 Project Overview
This project explores how **geography** influences Wikipedia edits across different languages. By analyzing edit patterns, we aim to uncover regional and linguistic disparities in digital knowledge representation.

🔍 **Key Insights:**
- Which regions contribute the most edits?
- How do editing behaviors vary across languages?
- What biases exist in content creation?
- How can we visualize these patterns interactively?

---

## 🎯 Objectives
✅ Investigate geographic distribution of Wikipedia edits  
✅ Compare edit trends across multiple languages  
✅ Identify biases and gaps in content creation  
✅ Build interactive visualizations for better insights  

---

## 📂 Dataset
📌 **Source:** Wikipedia Edit History API, Wikimedia dumps  
📊 **Data Includes:**
- 🌍 Editor locations (where available)
- 🕒 Edit timestamps
- 🔠 Language editions
- 📚 Article categories

---

## 🛠️ Tech Stack
🔹 **Programming:** Python 🐍  
🔹 **Data Analysis:** Pandas, NumPy 📊  
🔹 **Visualization:** Matplotlib, Seaborn, Plotly 📉  
🔹 **Geospatial Analysis:** GeoPandas, Folium 🌎  
🔹 **API & Scraping:** Wikipedia API, BeautifulSoup 🌐  

---

## 📌 Repository Structure
📂 **Data**  
- `Country_Language_List.csv` - Country-to-language mapping
- `Distance_metric.csv` - Computed distances between countries
- `filtered_dataset.csv` - Cleaned and preprocessed dataset

📜 **Scripts**  
- `Country_graph.py` - Generates graphs by country
- `Distance_metrics.py` - Computes country distances
- `Finalgraph_cal.py` - Final graph calculations
- `graph_similarity_metrics.py` - Graph similarity analysis

🖼️ **Visuals**  
- `Figure_1.png` to `Figure_6.png` - Data visualization snapshots
- `CalculationOutput.png` - Processed analysis results

📽️ **Presentation**  
- `Presentation 1-1.pptx` - Summary of project insights

---

## 🚀 Getting Started
### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/pranjaykumar926/SummerProject.git
 cd SummerProject
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then run:
```sh
 pip install pandas numpy matplotlib seaborn plotly geopandas folium
```

### 3️⃣ Run Analysis Scripts
Run any of the scripts to perform analyses or generate visualizations:
```sh
 python Country_graph.py
```

---
---

## 📅 Future Enhancements
🌟 Expand dataset to more language editions  
🤖 Implement machine learning for edit pattern prediction  
📊 Develop an interactive web-based dashboard  

---

## 🤝 Contributions
We welcome contributions! 🚀
1. **Fork the repository**
2. **Create a new branch** (`feature-branch`)
3. **Make your changes** and commit
4. **Submit a pull request**

---


---

🐙 **GitHub:** [pranjaykumar926](https://github.com/pranjaykumar926)  

🚀 _Happy Coding & Analyzing!_ 🎯
