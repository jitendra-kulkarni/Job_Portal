import { useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api/axios";



function ApplyJob() {

    const [resume, setResume] = useState(null);
    const [coverLetter, setCoverLetter] = useState("");
    const { id } = useParams();

    const handleSubmit = (e) => {
        e.preventDefault();

        const formData = new FormData();

        formData.append("job", id);
        formData.append("resume", resume);
        formData.append("cover_letter", coverLetter);

        api.post("applications/", formData)

            .then((response) => {

                console.log("Application Submitted");
                console.log(response.data);

            })

            .catch((error) => {

                console.log(error.response?.data);

            });

    };

    return (

        <form onSubmit={handleSubmit}>

            <input
                type="file"
                onChange={(e) => setResume(e.target.files[0])}
            />

            <br /><br />

            <textarea
                rows="6"
                placeholder="Write your cover letter..."
                value={coverLetter}
                onChange={(e) => setCoverLetter(e.target.value)}
            />

            <br /><br />

            <button>
                Apply
            </button>

        </form>
    )

}
export default ApplyJob;