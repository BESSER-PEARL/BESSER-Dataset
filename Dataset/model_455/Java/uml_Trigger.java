





import java.util.List;
import java.util.ArrayList;

public class uml_Trigger extends NamedElement {






    private uml_Transition uml_transition;




    private uml_Event uml_event;




    private uml_State uml_state;


    public uml_Trigger(
    ) {
        super(
        );
    }



    public uml_Transition getUml_transition() {
        return uml_transition;
    }

    public void setUml_transition(uml_Transition uml_transition) {
        this.uml_transition = uml_transition;
    }
    public uml_Event getUml_event() {
        return uml_event;
    }

    public void setUml_event(uml_Event uml_event) {
        this.uml_event = uml_event;
    }
    public uml_State getUml_state() {
        return uml_state;
    }

    public void setUml_state(uml_State uml_state) {
        this.uml_state = uml_state;
    }

}