





import java.util.List;
import java.util.ArrayList;

public class Position  {

    private String jobID;
    private String divisionName;
    private int positionID;
    private String positionName;





    private Applicant applicant;


    public Position(
        String jobID,        String divisionName,        int positionID,        String positionName    ) {
        this.jobID = jobID;
        this.divisionName = divisionName;
        this.positionID = positionID;
        this.positionName = positionName;
    }


    public String getJobid() {
        return jobID;
    }

    public void setJobid(String jobID) {
        this.jobID = jobID;
    }
    public String getDivisionname() {
        return divisionName;
    }

    public void setDivisionname(String divisionName) {
        this.divisionName = divisionName;
    }
    public int getPositionid() {
        return positionID;
    }

    public void setPositionid(int positionID) {
        this.positionID = positionID;
    }
    public String getPositionname() {
        return positionName;
    }

    public void setPositionname(String positionName) {
        this.positionName = positionName;
    }

    public Applicant getApplicant() {
        return applicant;
    }

    public void setApplicant(Applicant applicant) {
        this.applicant = applicant;
    }

}