const API_URL = process.env.REACT_APP_API_URL;

const generateReport = async () => {
  try {
    const response = await fetch(
      `${API_URL}/analyze-company`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          company_name: companyName,
          industry,
          revenue,
          employees,
          tech_stack: techStack,
          product_focus: productFocus,
          geography,
        }),
      }
    );

    const data = await response.json();

    if (data.report) {
      setReport(data.report);
    } else {
      setReport("No report generated.");
    }
  } catch (error) {
    console.error(error);
    setReport(
      "Something went wrong. Please make sure the backend is running."
    );
  }
};