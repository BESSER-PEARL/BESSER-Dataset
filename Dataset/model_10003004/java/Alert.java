





import java.util.List;
import java.util.ArrayList;

public class Alert  {

    private int AlertID;





    private Factory_Security_System factory_security_system;


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

    public Factory_Security_System getFactory_security_system() {
        return factory_security_system;
    }

    public void setFactory_security_system(Factory_Security_System factory_security_system) {
        this.factory_security_system = factory_security_system;
    }

}