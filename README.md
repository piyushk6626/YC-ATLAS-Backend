# 🚀 YC ATLAS Backend - AI-Powered YC Startup Search Engine

## 🔎 Discover YC Startups with AI: [YC ATLAS](https://yc-atlas.lovable.app/)

The **YC ATLAS Backend** is the API powerhouse behind **[YC ATLAS](https://yc-atlas.lovable.app/)**—an **AI-driven search engine** that helps researchers, investors, and entrepreneurs explore **Y Combinator startups** using advanced **semantic search and AI-powered query expansion**.

### 📌 Why YC ATLAS Backend?
✅ **AI-Enhanced YC Search** – Finds YC startups using natural language queries.

✅ **Multi-Step Agentic Search** – Expands queries with **LLM-powered reasoning**.

✅ **Vector Similarity Search** – Uses **text-embedding-3-large** for semantic search.

✅ **Super Fast API** – Built on **FastAPI** for high performance.

✅ **Scalable & Efficient** – Uses **Pinecone vector database** for lightning-fast retrieval.

---

## 🚀 Key Features

### 🔥 Advanced Search Functionality
- **Quick Search** – Finds relevant YC companies instantly based on a single query.
- **Deep Research** – Uses **multi-query AI expansion** for comprehensive results.

### 🤖 AI-Powered Search Flow
- **LLM-Powered Semantic Search** – Understands & refines user queries.
- **Query Expansion** – Generates multiple related questions to improve search depth.
- **Parallel Processing** – Executes multiple searches simultaneously for speed.

### 🔌 API Endpoints
| Endpoint | Description |
|----------|-------------|
| `/api/search_companies` | Single-query YC company search |
| `/api/deep_research` | Multi-query advanced search for deeper insights |
| `/api/company/:id` | Fetches details of a specific YC startup |

---

## 🛠️ Tech Stack
✅ **FastAPI** – Blazing-fast API framework  
✅ **OpenAI API** – AI-powered query enhancement & embeddings  
✅ **Pinecone** – Vector search for high-speed similarity retrieval  
✅ **Async & Parallel Processing** – Optimized for fast data processing  
✅ **Text-Embedding-3-Large** – Cutting-edge AI model for semantic search  

---

## ⚡ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/piyushk6626/YC-ATLAS-Backend.git
cd YC-ATLAS-Backend

# Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add API keys in .env:
# OPENAI_API_KEY=your_api_key
# PINECONE_API_KEY=your_api_key
# PINECONE_HOST_URL=your_pinecone_host_url
# MONGO_URI=your_mongodb_connection_string
```

### ▶️ Running the API Server
```bash
# Run with uvicorn
uvicorn app.main:app --reload
```
🔗 **API available at:** [http://localhost:8000](http://localhost:8000)  
🔗 **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)  
🔗 **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)  

---

## 🚀 Usage Examples

### 🔍 Quick Search
```python
import requests
response = requests.post("http://localhost:8000/api/search_companies", json={"query": "Company that works in RAG"})
print(response.json())
```

### 🤖 Deep Research
```python
import requests
response = requests.post("http://localhost:8000/api/deep_research", json={"query": "AI-driven YC startups"})
print(response.json())
```

### 🏢 Get Company Details
```python
import requests
response = requests.get("http://localhost:8000/api/company/CompanyName")
print(response.json())
```

---

## 📊 System Architecture

1️⃣ **User Query** – Input request from user  
2️⃣ **Query Expansion** – AI generates multiple related queries  
3️⃣ **Query Enhancement** – AI refines and optimizes queries  
4️⃣ **Embedding Generation** – Queries converted into vector embeddings  
5️⃣ **Parallel Search** – Conducts multiple similarity searches in parallel  
6️⃣ **Results Aggregation** – Merges results and ranks top matches  
7️⃣ **Final Output** – Returns a ranked list of **relevant YC startups**  

---

## 📂 Project Structure

```
YC-ATLAS-Backend/
├── app/                   # Main application package
│   ├── __init__.py        # Package initialization
│   ├── main.py            # FastAPI application entry point
│   ├── api/               # API-related code
│   │   ├── __init__.py
│   │   ├── models.py      # Pydantic models for API
│   │   └── routes/        # API route handlers
│   │       ├── __init__.py
│   │       ├── search.py  # Search-related endpoints
│   │       └── companies.py # Company data endpoints
│   ├── core/              # Core application code
│   │   ├── __init__.py
│   │   └── config.py      # Application configuration
│   ├── db/                # Database access layer
│   │   ├── __init__.py
│   │   └── company_data.py # Company data operations
│   ├── services/          # Service layer for external APIs
│   │   ├── __init__.py
│   │   ├── openai_service.py  # OpenAI API integration
│   │   ├── pinecone_service.py # Vector DB operations
│   │   └── prompts.py     # Prompts for LLM interactions
│   └── utils/             # Utility functions
│       ├── __init__.py
│       └── data_normalization.py # Data processing utilities
├── requirements.txt       # Project dependencies
├── .env.example           # Example environment variables
└── README.md              # Project documentation
```

---

## 🛠 Contributing

Contributions welcome! 🚀
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Added an awesome feature'`)
4. Push to GitHub (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 🔗 Related Repositories
- **[YC ATLAS Frontend](https://github.com/piyushk6626/YC-ATLAS-Frontend)** – React-based UI for YC ATLAS  
- **[YC ATLAS Scraper](https://github.com/piyushk6626/YC-ATLAS-Scraping)** – Data extraction & processing tools  

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 📩 Contact & Support
- **Creator**: [Piyush Kulkarni](https://github.com/piyushk6626)  
- **Have questions?** Open a GitHub Issue! 🚀  
- **🌟 Star this Repo on GitHub!** [GitHub Link](https://github.com/piyushk6626/YC-ATLAS-Backend)  

---

## 🔥 Why Use YC ATLAS Backend?
✅ **AI-Powered Search Engine** – Discover YC startups instantly.  
✅ **Multi-Agent Reasoning** – Enhances queries for deeper insights.  
✅ **Semantic Search Ready** – Uses **vector embeddings** for intelligent retrieval.  
✅ **Optimized for Speed & Scale** – Parallel & async processing for efficiency.  
✅ **SEO-Optimized** – Find YC startups faster with structured search.  

🚀 **Try it now:** [YC ATLAS](https://yc-atlas.lovable.app/) 🔥

