





import java.util.List;
import java.util.ArrayList;

public class RandL_Service  {

    private String description;
    private String pointsEarned;
    private String pointsBurned;
    private String serviceNr;
    private String condition;





    private RandL_ServiceLevel randl_servicelevel;




    private RandL_Container_RandL randl_container_randl;




    private RandL_ServiceLevel randl_servicelevel;


    public RandL_Service(
        String description,        String pointsEarned,        String pointsBurned,        String serviceNr,        String condition    ) {
        this.description = description;
        this.pointsEarned = pointsEarned;
        this.pointsBurned = pointsBurned;
        this.serviceNr = serviceNr;
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
    public String getPointsburned() {
        return pointsBurned;
    }

    public void setPointsburned(String pointsBurned) {
        this.pointsBurned = pointsBurned;
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
    public RandL_Container_RandL getRandl_container_randl() {
        return randl_container_randl;
    }

    public void setRandl_container_randl(RandL_Container_RandL randl_container_randl) {
        this.randl_container_randl = randl_container_randl;
    }
    public RandL_ServiceLevel getRandl_servicelevel() {
        return randl_servicelevel;
    }

    public void setRandl_servicelevel(RandL_ServiceLevel randl_servicelevel) {
        this.randl_servicelevel = randl_servicelevel;
    }

}