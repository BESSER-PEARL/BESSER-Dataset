





import java.util.List;
import java.util.ArrayList;

public class iotdsl_Transition  {

    private String name;





    private iotdsl_State iotdsl_state;




    private iotdsl_Event iotdsl_event;


    public iotdsl_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iotdsl_State getIotdsl_state() {
        return iotdsl_state;
    }

    public void setIotdsl_state(iotdsl_State iotdsl_state) {
        this.iotdsl_state = iotdsl_state;
    }
    public iotdsl_Event getIotdsl_event() {
        return iotdsl_event;
    }

    public void setIotdsl_event(iotdsl_Event iotdsl_event) {
        this.iotdsl_event = iotdsl_event;
    }

}