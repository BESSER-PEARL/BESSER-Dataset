





import java.util.List;
import java.util.ArrayList;

public class Alert  {

    private int AlertID;





    private Mobile_App mobile_app;


    public Alert(
        int AlertID    ) {
        this.AlertID = AlertID;
    }


    public int getAlertid() {
        return AlertID;
    }

    public void setAlertid(int AlertID) {
        this.AlertID = AlertID;
    }

    public Mobile_App getMobile_app() {
        return mobile_app;
    }

    public void setMobile_app(Mobile_App mobile_app) {
        this.mobile_app = mobile_app;
    }

}