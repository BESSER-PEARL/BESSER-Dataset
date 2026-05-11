





import java.util.List;
import java.util.ArrayList;

public class RandL_Service  {

    private String pointsBurned;
    private String pointsEarned;
    private String description;
    private String serviceNr;
    private String condition;





    private RandL_ServiceLevel randl_servicelevel;




    private RandL_ServiceLevel randl_servicelevel;


    public RandL_Service(
        String pointsBurned,        String pointsEarned,        String description,        String serviceNr,        String condition    ) {
        this.pointsBurned = pointsBurned;
        this.pointsEarned = pointsEarned;
        this.description = description;
        this.serviceNr = serviceNr;
        this.condition = condition;
    }


    public String getPointsburned() {
        return pointsBurned;
    }

    public void setPointsburned(String pointsBurned) {
        this.pointsBurned = pointsBurned;
    }
    public String getPointsearned() {
        return pointsEarned;
    }

    public void setPointsearned(String pointsEarned) {
        this.pointsEarned = pointsEarned;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getServicenr() {
        return serviceNr;
    }

    public void setServicenr(String serviceNr) {
        this.serviceNr = serviceNr;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
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