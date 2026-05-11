





import java.util.List;
import java.util.ArrayList;

public class workflow_IWorkflowJob extends IWorkflowNode {

    private String jobDescription;
    private String jobDescriptionFileName;



    public workflow_IWorkflowJob(
        String jobDescription,        String jobDescriptionFileName    ) {
        super(
        );
        this.jobDescription = jobDescription;
        this.jobDescriptionFileName = jobDescriptionFileName;
    }


    public String getJobdescription() {
        return jobDescription;
    }

    public void setJobdescription(String jobDescription) {
        this.jobDescription = jobDescription;
    }
    public String getJobdescriptionfilename() {
        return jobDescriptionFileName;
    }

    public void setJobdescriptionfilename(String jobDescriptionFileName) {
        this.jobDescriptionFileName = jobDescriptionFileName;
    }


}