import React, { useState } from "react";
import "./App.css";

function App() {
  const [companyName, setCompanyName] = useState("");
  const [industry, setIndustry] = useState("");
  const [arr, setArr] = useState("");
  const [employees, setEmployees] = useState("");
  const [techStack, setTechStack] = useState("");
  const [customers, setCustomers] = useState("");
  const [geography, setGeography] = useState("");

  const [report, setReport] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
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
          body: JSON.stringify({
            company_name: companyName,
            industry: industry,
            arr: arr,
            employees: employees,
            tech_stack: techStack,
            customers: customers,
            geography: geography,
          }),
        }
      );

      const data = await response.json();

      console.log(data);

      setReport(
        data.analysis ||
          data.report ||
          JSON.stringify(data, null, 2)
      );
    } catch (error) {
      console.error(error);
      setReport("Error generating report");
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="container">
        <h1>DealLens AI</h1>

        <div className="content">
          <div className="left-panel">
            <h2>Target Company Profile</h2>

            <input
              type="text"
              placeholder="Company Name"
              value={companyName}
              onChange={(e) => setCompanyName(e.target.value)}
            />

            <input
              type="text"
              placeholder="Industry"
              value={industry}
              onChange={(e) => setIndustry(e.target.value)}
            />

            <input
              type="text"
              placeholder="ARR / Revenue"
              value={arr}
              onChange={(e) => setArr(e.target.value)}
            />

            <input
              type="text"
              placeholder="Employees"
              value={employees}
              onChange={(e) => setEmployees(e.target.value)}
            />

            <input
              type="text"
              placeholder="Tech Stack"
              value={techStack}
              onChange={(e) => setTechStack(e.target.value)}
            />

            <input
              type="text"
              placeholder="Customers"
              value={customers}
              onChange={(e) => setCustomers(e.target.value)}
            />

            <input
              type="text"
              placeholder="Geography"
              value={geography}
              onChange={(e) => setGeography(e.target.value)}
            />

            <button onClick={handleGenerate}>
              {loading ? "Generating..." : "Generate Due Diligence Report"}
            </button>
          </div>

          <div className="right-panel">
            <h2>AI Due Diligence Report</h2>

            <div className="report-box">
              {loading ? (
                <p>Generating report...</p>
              ) : (
                <pre>{report}</pre>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;