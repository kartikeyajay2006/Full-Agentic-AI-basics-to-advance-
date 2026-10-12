<div align="center">

# 🧭 Agentic AI: From Basics to Advanced

**My hands-on notebook of code for learning LLM application development with LangChain. Each folder is one concept, and each file is a small program you can run.**

[![LangChain](https://img.shields.io/badge/LangChain-core-1C3C3C?style=flat-square&logo=langchain&logoColor=white)](https://python.langchain.com/)
[![Gemini](https://img.shields.io/badge/Google-Gemini_2.5_Flash-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)
[![Groq](https://img.shields.io/badge/Groq-Llama_3.1_8B-F55036?style=flat-square)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UIs-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pydantic](https://img.shields.io/badge/Pydantic-structured_output-E92063?style=flat-square&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)

</div>

---

## Learning path

| # | Module | What you learn | Files |
|---|---|---|---|
| 1 | **LLMs** | Call a chat model in a few lines and read the response | [`1.LLMs/1_llm_demo.py`](1.LLMs/1_llm_demo.py) |
| 2 | **Chatbots and memory** | Keep conversation history; use typed `SystemMessage`, `HumanMessage` and `AIMessage` | [`1_chatbot.py`](prompt_folder_llm/1_chatbot.py) · [`2_chatbot-message.py`](prompt_folder_llm/message-chatbot/2_chatbot-message.py) |
| 3 | **Prompt engineering** | `PromptTemplate` with variables, templates saved to and loaded from JSON, and choice of style (concise, detailed or step-by-step) and length | [`prompt_style.py`](prompt_folder_llm/prompt-style-loader/prompt_style.py) · [`prompt-better_option.py`](prompt_folder_llm/prompt-style-loader/prompt-better_option.py) |
| 4 | **Prompt UIs** | Put an LLM behind a Streamlit interface with input validation | [`prompt_ui.py`](prompt_folder_llm/prompt_ui.py) |
| 5 | **Embeddings and semantic search** | Embed documents with `text-embedding-004` and rank them against a query with cosine similarity, which is the core of RAG | [`3.EmbededModels/2_project-1.py`](3.EmbededModels/2_project-1.py) |
| 6 | **Structured output** | Get typed data back from an LLM using `TypedDict` and Pydantic models with field validation | [`structured_output_LLMs/`](structured_output_LLMs/) |

**Next modules:** output parsers → chains → RAG with a vector store → tools and tool-calling → LangGraph agents → multi-agent systems.

## Run any example

```bash
git clone https://github.com/kartikeyajay2006/Full-Agentic-AI-basics-to-advance-.git
cd Full-Agentic-AI-basics-to-advance-
pip install langchain-core langchain-google-genai langchain-groq streamlit pydantic[email] scikit-learn python-dotenv

# .env
echo "GOOGLE_API_KEY=..." >> .env
echo "GROQ_API_KEY=..."   >> .env

python 1.LLMs/1_llm_demo.py
streamlit run prompt_folder_llm/prompt_ui.py
```

## Where these ideas went next

The patterns practised here (structured output, embeddings and agent loops) power my larger projects:

- [AEGIS](https://github.com/kartikeyajay2006/Sovereign-On_Premise-Agentic-AI-Workbench): an air-gapped agentic AI workbench
- [EraseOps](https://github.com/kartikeyajay2006/Wispr_goa_task): LangGraph agents for GDPR erasure
- [Multimodal Evidence Console](https://github.com/kartikeyajay2006/Multimodal-Data-Management-Pipeline-for-RAG-Ready-Systems): graph RAG over video and PDFs

## Author

**[Kartikeya Yadav](https://github.com/kartikeyajay2006)** · [LinkedIn](https://www.linkedin.com/in/kartikeya2006/)
