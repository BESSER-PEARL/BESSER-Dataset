





import java.util.List;
import java.util.ArrayList;

public class gfsm_Transition  {

    private String event;





    private gfsm_Machine gfsm_machine;


    public gfsm_Transition(
        String event    ) {
        this.event = event;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public gfsm_Machine getGfsm_machine() {
        return gfsm_machine;
    }

    public void setGfsm_machine(gfsm_Machine gfsm_machine) {
        this.gfsm_machine = gfsm_machine;
    }

}