





import java.util.List;
import java.util.ArrayList;

public class RandL_Service  {

    private String serviceNr;
    private String pointsBurned;
    private String condition;
    private String description;
    private String pointsEarned;





    private RandL_ServiceLevel randl_servicelevel;




    private RandL_ServiceLevel randl_servicelevel;


    public RandL_Service(
        String serviceNr,        String pointsBurned,        String condition,        String description,        String pointsEarned    ) {
        this.serviceNr = serviceNr;
        this.pointsBurned = pointsBurned;
        this.condition = condition;
        this.description = description;
        this.pointsEarned = pointsEarned;
    }


    public String getServicenr() {
        return serviceNr;
    }

    public void setServicenr(String serviceNr) {
        this.serviceNr = serviceNr;
    }
    public String getPointsburned() {
        return pointsBurned;
    }

    public void setPointsburned(String pointsBurned) {
        this.pointsBurned = pointsBurned;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPointsearned() {
        return pointsEarned;
    }

    public void setPointsearned(String pointsEarned) {
        this.pointsEarned = pointsEarned;
    }

    public RandL_ServiceLevel getRandl_servicelevel() {
        return randl_servicelevel;
    }

    public void setRandl_servicelevel(RandL_ServiceLevel randl_servicelevel) {
        this.randl_servicelevel = randl_servicelevel;
    }
    public RandL_ServiceLevel getRandl_servicelevel() {
        return randl_servicelevel;
    }

    public void setRandl_servicelevel(RandL_ServiceLevel randl_servicelevel) {
        this.randl_servicelevel = randl_servicelevel;
    }

}