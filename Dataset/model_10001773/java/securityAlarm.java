





import java.util.List;
import java.util.ArrayList;

public class securityAlarm  {

    private boolean status;





    private Home_Security_System home_security_system;


    public securityAlarm(
        boolean status    ) {
        this.status = status;
    }


    public boolean getStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public Home_Security_System getHome_security_system() {
        return home_security_system;
    }

    public void setHome_security_system(Home_Security_System home_security_system) {
        this.home_security_system = home_security_system;
    }

}