





import java.util.List;
import java.util.ArrayList;

public class Alert  {

    private int AlertID;





    private Home_Security_System home_security_system;


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

    public Home_Security_System getHome_security_system() {
        return home_security_system;
    }

    public void setHome_security_system(Home_Security_System home_security_system) {
        this.home_security_system = home_security_system;
    }

}