





import java.util.List;
import java.util.ArrayList;

public class Position  {

    private int positionID;
    private String divisionName;
    private String positionName;
    private String jobID;





    private Applicant applicant;


    public Position(
        int positionID,        String divisionName,        String positionName,        String jobID    ) {
        this.positionID = positionID;
        this.divisionName = divisionName;
        this.positionName = positionName;
        this.jobID = jobID;
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
    public String getPositionname() {
        return positionName;
    }

    public void setPositionname(String positionName) {
        this.positionName = positionName;
    }
    public String getJobid() {
        return jobID;
    }

    public void setJobid(String jobID) {
        this.jobID = jobID;
    }

    public Applicant getApplicant() {
        return applicant;
    }

    public void setApplicant(Applicant applicant) {
        this.applicant = applicant;
    }

}