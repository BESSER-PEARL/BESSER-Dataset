





import java.util.List;
import java.util.ArrayList;

public class sooml_Transition  {






    private sooml_State sooml_state;




    private sooml_Guard sooml_guard;




    private sooml_Event sooml_event;




    private sooml_State sooml_state;




    private List<sooml_Action> sooml_actions;


    public sooml_Transition(
    ) {
        this.sooml_actions = new ArrayList<>();
    }

    public sooml_Transition(
        ArrayList<sooml_Action> sooml_actions    ) {
        this.sooml_actions = sooml_actions;
    }


    public sooml_State getSooml_state() {
        return sooml_state;
    }

    public void setSooml_state(sooml_State sooml_state) {
        this.sooml_state = sooml_state;
    }
    public sooml_Guard getSooml_guard() {
        return sooml_guard;
    }

    public void setSooml_guard(sooml_Guard sooml_guard) {
        this.sooml_guard = sooml_guard;
    }
    public sooml_Event getSooml_event() {
        return sooml_event;
    }

    public void setSooml_event(sooml_Event sooml_event) {
        this.sooml_event = sooml_event;
    }
    public sooml_State getSooml_state() {
        return sooml_state;
    }

    public void setSooml_state(sooml_State sooml_state) {
        this.sooml_state = sooml_state;
    }
    public List<sooml_Action> getSooml_actions() {
        return sooml_actions;
    }

    public void addSooml_action(Sooml_action sooml_action) {
        this.sooml_actions.add(sooml_action);
    }

}