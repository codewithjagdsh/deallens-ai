from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CompanyProfile(BaseModel):
    company_name: str
    industry: str
    arr: str
    employees: str
    tech_stack: str
    customers: str
    geography: str


@app.get("/")
def home():
    return {"message": "DealLens AI backend is running"}


@app.post("/analyze-company")
def analyze_company(profile: CompanyProfile):

    prompt = f"""
You are a Private Equity due diligence analyst.

Analyze this target company:

Company Name: {profile.company_name}
Industry: {profile.industry}
ARR: {profile.arr}
Employees: {profile.employees}
Technology Stack: {profile.tech_stack}
Customers: {profile.customers}
Geography: {profile.geography}

Generate a clean, readable PE due diligence report in HTML format.

Formatting rules:
- Use clean HTML tags only.
- Do not use markdown symbols like ###, **, or ---.
- Use headings, short paragraphs, and bullet points.
- Make it easy for business users and non-technical investors to read.
- Use simple but professional Private Equity language.
- Keep paragraphs short.
- Use bullet points wherever possible.

Required sections:

<h2>1. Executive Summary</h2>
Use 3 to 5 bullet points explaining:
<ul>
<li>What the company does</li>
<li>Why it is attractive</li>
<li>Main investment opportunity</li>
<li>Major concerns</li>
</ul>

<h2>2. Market Sizing & Competitive Positioning</h2>
Use bullet points for:
<ul>
<li>Market size</li>
<li>Growth drivers</li>
<li>Customer segment</li>
<li>Competitors</li>
<li>Competitive advantage</li>
</ul>

<h2>3. Technology Stack Assessment</h2>
Explain:
<ul>
<li>How modern the technology stack is</li>
<li>Scalability</li>
<li>Maintainability</li>
<li>Technical debt</li>
<li>Security or infrastructure concerns</li>
</ul>

<h2>4. AI Readiness</h2>
Explain:
<ul>
<li>Where AI can improve the product</li>
<li>Where AI can improve operations</li>
<li>Data availability</li>
<li>Automation opportunities</li>
<li>AI maturity level</li>
</ul>

<h2>5. Risk Matrix</h2>
Generate a properly aligned HTML table.

Use this exact table structure:

<table>
<tr>
<th>Risk</th>
<th>Severity</th>
<th>Explanation</th>
<th>Mitigation</th>
</tr>
<tr>
<td>Risk name</td>
<td>High / Medium / Low</td>
<td>Short explanation</td>
<td>Mitigation plan</td>
</tr>
</table>

Create at least 5 risks.
Risks should include technical debt, regulatory exposure, market competition, talent gap, and customer concentration.

<h2>6. Investment Recommendation</h2>
Clearly state one of:
<ul>
<li>Invest</li>
<li>Invest with Caution</li>
<li>Do Not Invest</li>
</ul>

Then explain the reasoning using bullet points.

<h2>7. Investment Memo</h2>
Create a short PE-style investment memo with these subheadings:

<h3>Investment Thesis</h3>
<ul>
<li>Explain why this company is worth considering.</li>
</ul>

<h3>Value Creation Plan</h3>
<ul>
<li>Explain growth, AI automation, product expansion, and operational improvements.</li>
</ul>

<h3>Key Risks</h3>
<ul>
<li>Summarize the most important investment risks.</li>
</ul>

<h3>Next Steps</h3>
<ul>
<li>Suggest due diligence actions before investment.</li>
</ul>
"""

    response = model.generate_content(prompt)

    return {
        "company_name": profile.company_name,
        "analysis": response.text
    }