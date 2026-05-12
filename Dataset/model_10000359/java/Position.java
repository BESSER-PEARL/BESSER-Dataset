





import java.util.List;
import java.util.ArrayList;

public class Position  {

    private String jobID;
    private String positionName;
    private int positionID;
    private String divisionName;





    private Applicant applicant;


    public Position(
        String jobID,        String positionName,        int positionID,        String divisionName    ) {
        this.jobID = jobID;
        this.positionName = positionName;
        this.positionID = positionID;
        this.divisionName = divisionName;
    }


    public String getJobid() {
        return jobID;
    }

    public void setJobid(String jobID) {
        this.jobID = jobID;
    }
    public String getPositionname() {
        return positionName;
    }

    public void setPositionname(String positionName) {
        this.positionName = positionName;
    }
    public int getPositionid() {
        return positionID;
    }

    public void setPositionid(int positionID) {
        this.positionID = positionID;
    }
    public String getDivisionname() {
        return divisionName;
    }

    public void setDivisionname(String divisionName) {
        this.divisionName = divisionName;
    }

    public Applicant getApplicant() {
        return applicant;
    }

    public void setApplicant(Applicant applicant) {
        this.applicant = applicant;
    }

}