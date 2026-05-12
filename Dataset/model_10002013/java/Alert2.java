





import java.util.List;
import java.util.ArrayList;

public class Alert2  {

    private int AlertID;





    private Web web;


    public Alert2(
        int AlertID    ) {
        this.AlertID = AlertID;
    }


    public int getAlertid() {
        return AlertID;
    }

    public void setAlertid(int AlertID) {
        this.AlertID = AlertID;
    }

    public Web getWeb() {
        return web;
    }

    public void setWeb(Web web) {
        this.web = web;
    }

}