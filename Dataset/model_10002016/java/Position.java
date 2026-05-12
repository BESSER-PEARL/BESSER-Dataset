





import java.util.List;
import java.util.ArrayList;

public class Position  {

    private String jobID;
    private String divisionName;
    private String positionName;
    private int positionID;



    public Position(
        String jobID,        String divisionName,        String positionName,        int positionID    ) {
        this.jobID = jobID;
        this.divisionName = divisionName;
        this.positionName = positionName;
        this.positionID = positionID;
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


}