





import java.util.List;
import java.util.ArrayList;

public class Position  {

    private String positionName;
    private String divisionName;
    private String jobID;
    private int positionID;





    private Applicant applicant;


    public Position(
        String positionName,        String divisionName,        String jobID,        int positionID    ) {
        this.positionName = positionName;
        this.divisionName = divisionName;
        this.jobID = jobID;
        this.positionID = positionID;
    }


    public String getPositionname() {
        return positionName;
    }

    public void setPositionname(String positionName) {
        this.positionName = positionName;
    }
    public String getDivisionname() {
        return divisionName;
    }

    public void setDivisionname(String divisionName) {
        this.divisionName = divisionName;
    }
    public String getJobid() {
        return jobID;
    }

    public void setJobid(String jobID) {
        this.jobID = jobID;
    }
    public int getPositionid() {
        return positionID;
    }

    public void setPositionid(int positionID) {
        this.positionID = positionID;
    }

    public Applicant getApplicant() {
        return applicant;
    }

    public void setApplicant(Applicant applicant) {
        this.applicant = applicant;
    }

}