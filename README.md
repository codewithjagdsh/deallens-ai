DealLens AI

AI-powered Private Equity Due Diligence Platform built for rapid company analysis and investment decision support.

Overview

DealLens AI is an end-to-end AI-assisted due diligence platform designed for Private Equity workflows. The application allows users to input a company profile and instantly generate an executive-ready diligence report covering:

Executive Summary
Market Sizing & Competitive Positioning
Technology Stack Assessment
AI Readiness Evaluation
Risk Matrix
Investment Recommendation
PE-style Investment Memo
Exportable PDF Report

The platform combines modern full-stack engineering with Generative AI to simulate the analytical workflow of PE analysts and investment associates.

Problem Statement

Private Equity firms often spend significant time conducting early-stage diligence on potential acquisitions. Traditional workflows require manual research across market reports, technical assessments, and strategic evaluations.

DealLens AI accelerates this process by generating structured AI-driven investment insights within seconds.

Key Features
AI-Powered Due Diligence
Generates structured investment analysis
Produces PE-style executive summaries
Evaluates AI integration opportunities
Identifies operational and technical risks
Professional Report Generation
Clean dashboard UI
Readable structured formatting
PDF export functionality
Executive-friendly presentation format
Dynamic Company Profiling

Users can input:

Company Name
Industry
ARR
Employee Count
Tech Stack
Customers
Geography

The system supports multiple industries including:

Healthcare
SaaS
Sports AI
FinTech
LegalTech
E-commerce
Enterprise AI
Tech Stack
Frontend
React.js
HTML5
CSS3
JavaScript
Backend
FastAPI
Python
AI Integration
Google Gemini API
Deployment
GitHub
Vercel (Frontend)
Render/Railway (Backend)
Architecture
Frontend (React)
        ↓
REST API Calls
        ↓
FastAPI Backend
        ↓
Gemini AI Model
        ↓
Generated Due Diligence Report
Folder Structure
deallens-ai/
│
├── backend/
│   ├── main.py
│   ├── .env
│   └── venv/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── node_modules/
│
└── .gitignore
Installation
Clone Repository
git clone https://github.com/codewithjagdsh/deallens-ai.git
cd deallens-ai
Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn python-dotenv google-generativeai

Create .env

GEMINI_API_KEY=YOUR_API_KEY

Run backend:

uvicorn main:app --reload

Backend runs on:

http://127.0.0.1:8000
Frontend Setup
cd frontend
npm install
npm start

Frontend runs on:

http://localhost:3000
API Endpoint
POST /analyze_company

Accepts:

{
  "company_name": "MedFlow AI",
  "industry": "Healthcare SaaS",
  "arr": "$15M",
  "employees": "120",
  "tech_stack": "React, Node.js, PostgreSQL, AWS",
  "customers": "Mid-market hospitals",
  "geography": "United States"
}

Returns:

Structured AI-generated diligence report
Sample Use Cases
Healthcare SaaS

AI-powered hospital workflow analysis.

Sports Analytics AI

Football scouting and performance prediction platforms.

LegalTech

AI petition drafting and legal document automation.

FinTech

Risk intelligence and fraud analytics startups.

Future Improvements
Live market data integration
Competitor benchmarking APIs
Financial valuation engine
Risk scoring dashboard
Multi-page PDF exports
Authentication & user accounts
Investment committee workflow
Project Highlights
Full-stack AI application
Real-world PE use case
Executive-ready reporting
Production-style architecture
Interactive UI/UX
Dynamic AI-generated insights
Author
Jagadeesh Rajapan

AI Engineer | Data Science & Full Stack AI Development

GitHub:
https://github.com/codewithjagdsh

License

This project is built for educational, portfolio, and assessment purposes.
