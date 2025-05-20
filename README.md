
---

## 🎬 Movie Recommendation System

```markdown
# 🎬 Movie Recommendation System

A simple **content-based movie recommendation system** built using **Python** and **Streamlit**. It recommends similar movies based on the selected movie's overview and genre using **cosine similarity** and **TF-IDF vectorization**.

---

## 🚀 Features

- Recommends top 5 similar movies from dataset
- Uses **TF-IDF** and **cosine similarity** for recommendations
- Clean and interactive Streamlit UI
- Movie poster previews using TMDB API (optional)

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit**
- **Scikit-learn** (`TfidfVectorizer`, `cosine_similarity`)
- **Pandas & Numpy**
- **TMDB API** (optional for posters)

---

## 📦 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/movie-recommendation-app.git
cd movie-recommendation-app

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
