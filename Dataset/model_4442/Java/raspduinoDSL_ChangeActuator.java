





import java.util.List;
import java.util.ArrayList;

public class raspduinoDSL_ChangeActuator  {

    private String ActuatorState;





    private raspduinoDSL_Actuator raspduinodsl_actuator;


    public raspduinoDSL_ChangeActuator(
        String ActuatorState    ) {
        this.ActuatorState = ActuatorState;
    }


    public String getActuatorstate() {
        return ActuatorState;
    }

    public void setActuatorstate(String ActuatorState) {
        this.ActuatorState = ActuatorState;
    }

    public raspduinoDSL_Actuator getRaspduinodsl_actuator() {
        return raspduinodsl_actuator;
    }

    public void setRaspduinodsl_actuator(raspduinoDSL_Actuator raspduinodsl_actuator) {
        this.raspduinodsl_actuator = raspduinodsl_actuator;
    }

}