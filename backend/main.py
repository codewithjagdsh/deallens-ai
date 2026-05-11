from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

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
You are a senior Private Equity due diligence analyst preparing an executive-ready investment report for PE partners.

Target Company:
Company Name: {profile.company_name}
Industry: {profile.industry}
ARR / Revenue: {profile.arr}
Employees: {profile.employees}
Technology Stack: {profile.tech_stack}
Customers: {profile.customers}
Geography: {profile.geography}

Generate a polished PE due diligence report in clean HTML format only.

Important formatting rules:
- Return only HTML body content.
- Do not include markdown.
- Do not include ```html.
- Do not include <html>, <head>, or <body>.
- Use clear headings, short paragraphs, bullet points, and tables.
- Make the language professional but easy to understand.
- Write for PE partners, investment analysts, and operating partners.
- Avoid vague generic statements.
- Use practical investment reasoning.

Required report structure:

<h2>1. Executive Summary</h2>
<ul>
<li>Summarize what the company does.</li>
<li>Explain the investment opportunity.</li>
<li>Mention the key strengths.</li>
<li>Mention the main risks.</li>
<li>Give a concise overall investment view.</li>
</ul>

<h2>2. Market Sizing & Competitive Positioning</h2>

<table>
<tr>
<th>Area</th>
<th>Analysis</th>
</tr>

<tr>
<td>Market Opportunity</td>
<td>Explain the size and attractiveness of the market.</td>
</tr>

<tr>
<td>Growth Drivers</td>
<td>List the main factors pushing market growth.</td>
</tr>

<tr>
<td>Customer Segment</td>
<td>Explain who buys this product and why.</td>
</tr>

<tr>
<td>Competitive Landscape</td>
<td>Explain likely competitors and market pressure.</td>
</tr>

<tr>
<td>Differentiation</td>
<td>Explain how the target can stand apart.</td>
</tr>
</table>

<h2>3. Competitive Landscape</h2>

<table>
<tr>
<th>Competitor Type</th>
<th>Strength</th>
<th>Weakness</th>
<th>Implication for Target</th>
</tr>

<tr>
<td>Large incumbents</td>
<td>Strong brand and distribution.</td>
<td>Legacy systems and slower innovation.</td>
<td>Target can compete using speed and AI differentiation.</td>
</tr>

<tr>
<td>AI-native startups</td>
<td>Modern AI-first products.</td>
<td>Limited enterprise scale.</td>
<td>Target must build defensibility and customer trust.</td>
</tr>

<tr>
<td>Internal enterprise tools</td>
<td>Domain-specific customization.</td>
<td>Poor scalability and maintenance.</td>
<td>Target can offer scalable SaaS automation.</td>
</tr>
</table>

<h2>4. Technology Stack Assessment</h2>

<table>
<tr>
<th>Category</th>
<th>Assessment</th>
<th>PE Interpretation</th>
</tr>

<tr>
<td>Frontend / Product Experience</td>
<td>Assess usability and modernity.</td>
<td>Better UX improves retention and expansion.</td>
</tr>

<tr>
<td>Backend Scalability</td>
<td>Assess scalability of architecture.</td>
<td>Scalable backend lowers future infrastructure risk.</td>
</tr>

<tr>
<td>Data Infrastructure</td>
<td>Assess data maturity and analytics readiness.</td>
<td>Strong data foundation improves AI upside.</td>
</tr>

<tr>
<td>Security & Reliability</td>
<td>Assess operational reliability and security posture.</td>
<td>Security issues create diligence risk.</td>
</tr>

<tr>
<td>Technical Debt</td>
<td>Assess modernization needs.</td>
<td>Technical debt affects valuation and integration costs.</td>
</tr>
</table>

<h2>5. AI Readiness Scorecard</h2>

<table>
<tr>
<th>Dimension</th>
<th>Score / 10</th>
<th>Rationale</th>
</tr>

<tr>
<td>Data Availability</td>
<td>Give realistic score</td>
<td>Explain quality and availability of data.</td>
</tr>

<tr>
<td>Automation Potential</td>
<td>Give realistic score</td>
<td>Explain workflow automation opportunities.</td>
</tr>

<tr>
<td>Product AI Opportunity</td>
<td>Give realistic score</td>
<td>Explain AI product enhancement opportunities.</td>
</tr>

<tr>
<td>Operational AI Opportunity</td>
<td>Give realistic score</td>
<td>Explain internal operational improvements.</td>
</tr>

<tr>
<td>Implementation Complexity</td>
<td>Give realistic score</td>
<td>Explain implementation difficulty.</td>
</tr>
</table>

<h2>6. Risk Matrix</h2>

<table>
<tr>
<th>Risk</th>
<th>Severity</th>
<th>Explanation</th>
<th>Mitigation</th>
</tr>

<tr>
<td>Technical Debt</td>
<td>High / Medium / Low</td>
<td>Explain the technical risk.</td>
<td>Suggest mitigation.</td>
</tr>

<tr>
<td>Regulatory Exposure</td>
<td>High / Medium / Low</td>
<td>Explain regulatory or compliance risk.</td>
<td>Suggest mitigation.</td>
</tr>

<tr>
<td>Talent Gap</td>
<td>High / Medium / Low</td>
<td>Explain hiring or capability risk.</td>
<td>Suggest mitigation.</td>
</tr>

<tr>
<td>Customer Concentration</td>
<td>High / Medium / Low</td>
<td>Explain revenue dependency risk.</td>
<td>Suggest mitigation.</td>
</tr>

<tr>
<td>Competitive Pressure</td>
<td>High / Medium / Low</td>
<td>Explain competitor pressure risk.</td>
<td>Suggest mitigation.</td>
</tr>
</table>

<h2>7. Investment Recommendation</h2>

<p><strong>Recommendation:</strong> Choose one: Invest, Invest with Caution, or Do Not Invest.</p>

<ul>
<li>Explain the primary investment rationale.</li>
<li>Explain growth opportunities.</li>
<li>Explain major concerns.</li>
<li>Explain what investors should validate next.</li>
</ul>

<h2>8. PE Partner Investment Memo</h2>

<h3>Investment Thesis</h3>

<p>Write a concise PE-style investment thesis explaining why this company deserves evaluation.</p>

<h3>Value Creation Plan</h3>

<ul>
<li>Revenue growth opportunities.</li>
<li>AI automation opportunities.</li>
<li>Product expansion opportunities.</li>
<li>Operational efficiency improvements.</li>
</ul>

<h3>Key Diligence Questions</h3>

<ul>
<li>List customer, technical, operational, and financial diligence questions.</li>
</ul>

<h3>Conclusion</h3>

<p>Provide a concise PE-partner-style final conclusion.</p>
"""

    response = model.generate_content(prompt)

    return {
        "company_name": profile.company_name,
        "analysis": response.text
    }