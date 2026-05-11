





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_Service  {

    private String description;
    private boolean condition;
    private int serviceNr;
    private int pointsBurned;
    private int pointsEarned;





    private RoyalAndLoyal_ServiceLevel royalandloyal_servicelevel;




    private RoyalAndLoyal_ServiceLevel royalandloyal_servicelevel;


    public RoyalAndLoyal_Service(
        String description,        boolean condition,        int serviceNr,        int pointsBurned,        int pointsEarned    ) {
        this.description = description;
        this.condition = condition;
        this.serviceNr = serviceNr;
        this.pointsBurned = pointsBurned;
        this.pointsEarned = pointsEarned;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getCondition() {
        return condition;
    }

    public void setCondition(boolean condition) {
        this.condition = condition;
    }
    public int getServicenr() {
        return serviceNr;
    }

    public void setServicenr(int serviceNr) {
        this.serviceNr = serviceNr;
    }
    public int getPointsburned() {
        return pointsBurned;
    }

    public void setPointsburned(int pointsBurned) {
        this.pointsBurned = pointsBurned;
    }
    public int getPointsearned() {
        return pointsEarned;
    }

    public void setPointsearned(int pointsEarned) {
        this.pointsEarned = pointsEarned;
    }

    public RoyalAndLoyal_ServiceLevel getRoyalandloyal_servicelevel() {
        return royalandloyal_servicelevel;
    }

    public void setRoyalandloyal_servicelevel(RoyalAndLoyal_ServiceLevel royalandloyal_servicelevel) {
        this.royalandloyal_servicelevel = royalandloyal_servicelevel;
    }
    public RoyalAndLoyal_ServiceLevel getRoyalandloyal_servicelevel() {
        return royalandloyal_servicelevel;
    }

    public void setRoyalandloyal_servicelevel(RoyalAndLoyal_ServiceLevel royalandloyal_servicelevel) {
        this.royalandloyal_servicelevel = royalandloyal_servicelevel;
    }

}