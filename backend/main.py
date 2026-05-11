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
    allow_credentials=False,
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
- Use bullet points wherever possible.

Required sections:

<h2>1. Executive Summary</h2>
<ul>
<li>Explain what the company does.</li>
<li>Explain why it is attractive.</li>
<li>Explain the main investment opportunity.</li>
<li>Explain major concerns.</li>
</ul>

<h2>2. Market Sizing & Competitive Positioning</h2>
<ul>
<li>Market size</li>
<li>Growth drivers</li>
<li>Customer segment</li>
<li>Competitors</li>
<li>Competitive advantage</li>
</ul>

<h2>3. Technology Stack Assessment</h2>
<ul>
<li>Technology maturity</li>
<li>Scalability</li>
<li>Maintainability</li>
<li>Technical debt</li>
<li>Security or infrastructure concerns</li>
</ul>

<h2>4. AI Readiness</h2>
<ul>
<li>AI product opportunities</li>
<li>AI operational opportunities</li>
<li>Data availability</li>
<li>Automation potential</li>
<li>AI maturity level</li>
</ul>

<h2>5. Risk Matrix</h2>
<table>
<tr>
<th>Risk</th>
<th>Severity</th>
<th>Explanation</th>
<th>Mitigation</th>
</tr>
<tr>
<td>Technical Debt</td>
<td>Medium</td>
<td>Assess scalability and maintainability risks.</td>
<td>Run technical audit and refactor critical systems.</td>
</tr>
<tr>
<td>Regulatory Exposure</td>
<td>High</td>
<td>Industry or geography may create compliance obligations.</td>
<td>Conduct legal and compliance due diligence.</td>
</tr>
<tr>
<td>Market Competition</td>
<td>Medium</td>
<td>Competitors may reduce pricing power.</td>
<td>Differentiate using AI features and customer success.</td>
</tr>
<tr>
<td>Talent Gap</td>
<td>Medium</td>
<td>Small teams may lack senior AI or infrastructure talent.</td>
<td>Hire senior engineering and AI leadership.</td>
</tr>
<tr>
<td>Customer Concentration</td>
<td>Medium</td>
<td>Revenue may depend on limited customer segments.</td>
<td>Diversify customer base and expand sales channels.</td>
</tr>
</table>

<h2>6. Investment Recommendation</h2>
<p>Clearly state one of: Invest, Invest with Caution, or Do Not Invest.</p>
<ul>
<li>Explain the recommendation.</li>
<li>Explain the upside.</li>
<li>Explain the downside.</li>
<li>Explain what must be validated before investment.</li>
</ul>

<h2>7. Investment Memo</h2>

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