





import java.util.List;
import java.util.ArrayList;

public class tfsm_TFSM extends NamedElement {






    private List<tfsm_FSMEvent> tfsm_fsmevents;




    private tfsm_State tfsm_state;




    private tfsm_State tfsm_state;




    private List<tfsm_State> tfsm_states;




    private tfsm_State tfsm_state;


    public tfsm_TFSM(
    ) {
        super(
        );
        this.tfsm_fsmevents = new ArrayList<>();
        this.tfsm_states = new ArrayList<>();
    }

    public tfsm_TFSM(
        ArrayList<tfsm_FSMEvent> tfsm_fsmevents,        ArrayList<tfsm_State> tfsm_states    ) {
        this.tfsm_fsmevents = tfsm_fsmevents;
        this.tfsm_states = tfsm_states;
    }


    public List<tfsm_FSMEvent> getTfsm_fsmevents() {
        return tfsm_fsmevents;
    }

    public void addTfsm_fsmevent(Tfsm_fsmevent tfsm_fsmevent) {
        this.tfsm_fsmevents.add(tfsm_fsmevent);
    }
    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }
    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }
    public List<tfsm_State> getTfsm_states() {
        return tfsm_states;
    }

    public void addTfsm_state(Tfsm_state tfsm_state) {
        this.tfsm_states.add(tfsm_state);
    }
    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }

}