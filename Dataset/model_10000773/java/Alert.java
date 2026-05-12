





import java.util.List;
import java.util.ArrayList;

public class Alert  {

    private int AlertID;





    private Security_System security_system;


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

    public Security_System getSecurity_system() {
        return security_system;
    }

    public void setSecurity_system(Security_System security_system) {
        this.security_system = security_system;
    }

}