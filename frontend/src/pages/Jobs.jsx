import { useEffect, useState } from "react";
import api from "../api/axios";
import "./Jobs.css";

function Jobs() {
    const [jobs, setJobs] = useState([]);

    useEffect(() => {
        api
            .get("jobs/")
            .then((response) => {
                setJobs(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    console.log(jobs);

    return (
        <div className="jobs-container">
            <h1>Available Jobs</h1>

            {jobs.map((job) => (
                <div className="job-card" key={job.id}>
                    <h2>{job.title}</h2>

                    <p>
                        <strong>🏢 Company:</strong> {job.company_name}
                    </p>

                    <p>📍 {job.location}</p>

                    <p>💰 ₹{job.salary}</p>

                    <p>💼 {job.employment_type}</p>

                    <p>🎯 {job.experience_level}</p>

                    <button>Apply Now</button>
                </div>
            ))}
        </div>
    );
}

export default Jobs;