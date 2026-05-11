





import java.util.List;
import java.util.ArrayList;

public class gfsm_Guard  {

    private String value;





    private gfsm_Transition gfsm_transition;


    public gfsm_Guard(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public gfsm_Transition getGfsm_transition() {
        return gfsm_transition;
    }

    public void setGfsm_transition(gfsm_Transition gfsm_transition) {
        this.gfsm_transition = gfsm_transition;
    }

}