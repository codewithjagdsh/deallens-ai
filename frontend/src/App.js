import { useState } from "react";
import "./App.css";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";

function App() {
  const [formData, setFormData] = useState({
    company_name: "",
    industry: "",
    arr: "",
    employees: "",
    tech_stack: "",
    customers: "",
    geography: ""
  });

  const [analysis, setAnalysis] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const analyzeCompany = async () => {
    setLoading(true);
    setAnalysis("");

    try {
      const response = await fetch("https://deallens-ai-backend-1.onrender.com/analyze-company", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
      });

      const data = await response.json();
      setAnalysis(data.analysis);
    } catch (error) {
      setAnalysis("<p>Something went wrong. Please make sure the backend is running.</p>");
    }

    setLoading(false);
  };

  const downloadPDF = async () => {
    const input = document.getElementById("report");

    const canvas = await html2canvas(input, {
      scale: 2,
      useCORS: true,
      scrollY: -window.scrollY,
      windowWidth: input.scrollWidth,
      windowHeight: input.scrollHeight
    });

    const imgData = canvas.toDataURL("image/png");

    const pdf = new jsPDF("p", "mm", "a4");

    const pdfWidth = 210;
    const pdfHeight = 297;

    const imgWidth = pdfWidth;
    const imgHeight = (canvas.height * imgWidth) / canvas.width;

    let heightLeft = imgHeight;
    let position = 0;

    pdf.addImage(imgData, "PNG", 0, position, imgWidth, imgHeight);

    heightLeft -= pdfHeight;

    while (heightLeft > 0) {
      position = heightLeft - imgHeight;
      pdf.addPage();
      pdf.addImage(imgData, "PNG", 0, position, imgWidth, imgHeight);
      heightLeft -= pdfHeight;
    }

    pdf.save(`${formData.company_name || "Due_Diligence_Report"}_Report.pdf`);
  };

  return (
    <div className="app">
      <div className="hero">
        <div>
          <p className="badge">AI-Powered Private Equity Intelligence</p>

          <h1>DealLens AI</h1>

          <p className="subtitle">
            Generate executive-ready due diligence, market intelligence,
            AI readiness analysis, risk matrices, and PE investment memos in seconds.
          </p>
        </div>
      </div>

      <div className="container">
        <div className="card form-card">
          <h2>Target Company Profile</h2>

          <p className="muted">
            Enter company information to generate a PE-style AI due diligence package.
          </p>

          <div className="grid">
            <input
              name="company_name"
              placeholder="Company Name"
              value={formData.company_name}
              onChange={handleChange}
            />

            <input
              name="industry"
              placeholder="Industry"
              value={formData.industry}
              onChange={handleChange}
            />

            <input
              name="arr"
              placeholder="ARR / Revenue"
              value={formData.arr}
              onChange={handleChange}
            />

            <input
              name="employees"
              placeholder="Employees"
              value={formData.employees}
              onChange={handleChange}
            />

            <input
              name="tech_stack"
              placeholder="Technology Stack"
              value={formData.tech_stack}
              onChange={handleChange}
            />

            <input
              name="customers"
              placeholder="Customer Segment"
              value={formData.customers}
              onChange={handleChange}
            />

            <input
              name="geography"
              placeholder="Geography"
              value={formData.geography}
              onChange={handleChange}
            />
          </div>

          <button onClick={analyzeCompany} disabled={loading}>
            {loading ? "Generating Analysis..." : "Generate Due Diligence Report"}
          </button>

          {analysis && !loading && (
            <button className="pdf-btn" onClick={downloadPDF}>
              Download PDF Report
            </button>
          )}
        </div>

        <div className="card report-card">
          <div className="report-header">
            <div>
              <h2>AI Due Diligence Report</h2>

              <p className="report-subtitle">
                Executive-ready PE investment analysis
              </p>
            </div>

            <div className="status">
              AI Generated
            </div>
          </div>

          {!analysis && !loading && (
            <div className="empty">
              Your investment analysis will appear here after generation.
            </div>
          )}

          {loading && (
            <div className="loading">
              <div className="spinner"></div>

              <p>
                Running AI analysis across market, technology,
                risk, and investment dimensions...
              </p>
            </div>
          )}

          {analysis && !loading && (
            <div id="report" className="analysis-content">
              <div dangerouslySetInnerHTML={{ __html: analysis }}></div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;