





import java.util.List;
import java.util.ArrayList;

public class tfsm_Transition extends NamedElement {

    private String action;





    private List<tfsm_FSMEvent> tfsm_fsmevents;




    private tfsm_FSMEvent tfsm_fsmevent;


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

    public List<tfsm_FSMEvent> getTfsm_fsmevents() {
        return tfsm_fsmevents;
    }

    public void addTfsm_fsmevent(Tfsm_fsmevent tfsm_fsmevent) {
        this.tfsm_fsmevents.add(tfsm_fsmevent);
    }
    public tfsm_FSMEvent getTfsm_fsmevent() {
        return tfsm_fsmevent;
    }

    public void setTfsm_fsmevent(tfsm_FSMEvent tfsm_fsmevent) {
        this.tfsm_fsmevent = tfsm_fsmevent;
    }

}