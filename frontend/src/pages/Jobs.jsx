import { useEffect, useState } from "react";
import api from "../api/axios";
import "./Jobs.css";
import { Link } from "react-router-dom";

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

                    <Link to={`/apply/${job.id}`}>
                        <button>Apply Now</button>
                    </Link>
                </div>
            ))}
        </div>
    );
}

export default Jobs;