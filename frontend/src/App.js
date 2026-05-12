import "./App.css";
import { useState } from "react";

function App() {
  const [formData, setFormData] = useState({
    company_name: "",
    industry: "",
    arr: "",
    employees: "",
    tech_stack: "",
    customers: "",
    geography: "",
  });

  const [report, setReport] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const generateReport = async () => {
    setLoading(true);
    setReport("");

    try {
      const response = await fetch(
        "https://deallens-ai-backend-1.onrender.com/analyze-company",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        }
      );

      const data = await response.json();

      setReport(data.analysis || "No report generated.");
    } catch (error) {
      setReport("Something went wrong. Please try again.");
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="header">
        <h1>DealLens AI</h1>
        <p>
          Generate executive-ready due diligence, market intelligence,
          AI readiness analysis, risk matrices, and PE investment memos.
        </p>
      </div>

      <div className="main-container">
        <div className="form-section">
          <h2>Target Company Profile</h2>

          <div className="form-group">
            <label>Company Name</label>
            <input
              type="text"
              name="company_name"
              value={formData.company_name}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Industry</label>
            <input
              type="text"
              name="industry"
              value={formData.industry}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>ARR</label>
            <input
              type="text"
              name="arr"
              value={formData.arr}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Employees</label>
            <input
              type="text"
              name="employees"
              value={formData.employees}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Tech Stack</label>
            <input
              type="text"
              name="tech_stack"
              value={formData.tech_stack}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Customers</label>
            <input
              type="text"
              name="customers"
              value={formData.customers}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Geography</label>
            <input
              type="text"
              name="geography"
              value={formData.geography}
              onChange={handleChange}
            />
          </div>

          <button className="generate-btn" onClick={generateReport}>
            Generate Due Diligence Report
          </button>
        </div>

        <div className="report-section">
          <div className="ai-badge">AI Generated</div>

          <h2>AI Due Diligence Report</h2>

          {loading ? (
            <div className="loading">Generating report...</div>
          ) : (
            <div
              className="report-box"
              dangerouslySetInnerHTML={{ __html: report }}
            />
          )}
        </div>
      </div>
    </div>
  );
}

export default App;