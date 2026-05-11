





import java.util.List;
import java.util.ArrayList;

public class ddsm_ClientNode extends InternalComponent {

    private boolean skipRunningJob;
    private int numberOfSubmissions;





    private ddsm_JobSubmission ddsm_jobsubmission;


    public ddsm_ClientNode(
        boolean skipRunningJob,        int numberOfSubmissions    ) {
        super(
        );
        this.skipRunningJob = skipRunningJob;
        this.numberOfSubmissions = numberOfSubmissions;
    }


    public boolean getSkiprunningjob() {
        return skipRunningJob;
    }

    public void setSkiprunningjob(boolean skipRunningJob) {
        this.skipRunningJob = skipRunningJob;
    }
    public int getNumberofsubmissions() {
        return numberOfSubmissions;
    }

    public void setNumberofsubmissions(int numberOfSubmissions) {
        this.numberOfSubmissions = numberOfSubmissions;
    }

    public ddsm_JobSubmission getDdsm_jobsubmission() {
        return ddsm_jobsubmission;
    }

    public void setDdsm_jobsubmission(ddsm_JobSubmission ddsm_jobsubmission) {
        this.ddsm_jobsubmission = ddsm_jobsubmission;
    }

}