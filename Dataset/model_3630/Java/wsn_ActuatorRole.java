





import java.util.List;
import java.util.ArrayList;

public class wsn_ActuatorRole extends Lifeline,  {






    private wsn_Actuator wsn_actuator;


    public wsn_ActuatorRole(
    ) {
        super(
        );
    }



    public wsn_Actuator getWsn_actuator() {
        return wsn_actuator;
    }

    public void setWsn_actuator(wsn_Actuator wsn_actuator) {
        this.wsn_actuator = wsn_actuator;
    }

}