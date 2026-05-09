





import java.util.List;
import java.util.ArrayList;

public class tfsm_Transition extends NamedElement {

    private String action;





    private tfsm_State tfsm_state;




    private tfsm_TFSM tfsm_tfsm;




    private tfsm_FSMEvent tfsm_fsmevent;




    private tfsm_State tfsm_state;




    private tfsm_Guard tfsm_guard;




    private tfsm_State tfsm_state;




    private tfsm_State tfsm_state;




    private List<tfsm_FSMEvent> tfsm_fsmevents;


    public tfsm_Transition(
        String action    ) {
        super(
        );
        this.action = action;
        this.tfsm_fsmevents = new ArrayList<>();
    }

    public tfsm_Transition(
        String action        ArrayList<tfsm_FSMEvent> tfsm_fsmevents    ) {
        this.action = action;
        this.tfsm_fsmevents = tfsm_fsmevents;
    }

    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }
    public tfsm_TFSM getTfsm_tfsm() {
        return tfsm_tfsm;
    }

    public void setTfsm_tfsm(tfsm_TFSM tfsm_tfsm) {
        this.tfsm_tfsm = tfsm_tfsm;
    }
    public tfsm_FSMEvent getTfsm_fsmevent() {
        return tfsm_fsmevent;
    }

    public void setTfsm_fsmevent(tfsm_FSMEvent tfsm_fsmevent) {
        this.tfsm_fsmevent = tfsm_fsmevent;
    }
    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }
    public tfsm_Guard getTfsm_guard() {
        return tfsm_guard;
    }

    public void setTfsm_guard(tfsm_Guard tfsm_guard) {
        this.tfsm_guard = tfsm_guard;
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
    public List<tfsm_FSMEvent> getTfsm_fsmevents() {
        return tfsm_fsmevents;
    }

    public void addTfsm_fsmevent(Tfsm_fsmevent tfsm_fsmevent) {
        this.tfsm_fsmevents.add(tfsm_fsmevent);
    }

}