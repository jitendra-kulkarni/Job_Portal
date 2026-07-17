import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api/axios";


function JobDetails (){
    const { id } = useParams();

    const [job, setjob] = useState(null);

    useEffect(() => {
        api.get(`jobs/${id}/`)
            .then((response) => {
                setjob(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
    }, [id]);

    if (!job) {
        return <h1> Loading......</h1>
    }

    return(
        <div>
            <h1>{job.title}</h1>

            <h3>{job.company_name}</h3>

            <p>{job.location}</p>

            <p>{job.salary}</p>
        </div>
    );
}

export default JobDetails;