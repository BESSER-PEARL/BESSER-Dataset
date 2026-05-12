





import java.util.List;
import java.util.ArrayList;

public class tfsm_plaink3_Transition extends NamedElement {

    private String action;





    private tfsm_plaink3_FSMEvent tfsm_plaink3_fsmevent;




    private List<tfsm_plaink3_FSMEvent> tfsm_plaink3_fsmevents;


    public tfsm_plaink3_Transition(
        String action    ) {
        super(
        );
        this.action = action;
        this.tfsm_plaink3_fsmevents = new ArrayList<>();
    }

    public tfsm_plaink3_Transition(
        String action        ArrayList<tfsm_plaink3_FSMEvent> tfsm_plaink3_fsmevents    ) {
        this.action = action;
        this.tfsm_plaink3_fsmevents = tfsm_plaink3_fsmevents;
    }

    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public tfsm_plaink3_FSMEvent getTfsm_plaink3_fsmevent() {
        return tfsm_plaink3_fsmevent;
    }

    public void setTfsm_plaink3_fsmevent(tfsm_plaink3_FSMEvent tfsm_plaink3_fsmevent) {
        this.tfsm_plaink3_fsmevent = tfsm_plaink3_fsmevent;
    }
    public List<tfsm_plaink3_FSMEvent> getTfsm_plaink3_fsmevents() {
        return tfsm_plaink3_fsmevents;
    }

    public void addTfsm_plaink3_fsmevent(Tfsm_plaink3_fsmevent tfsm_plaink3_fsmevent) {
        this.tfsm_plaink3_fsmevents.add(tfsm_plaink3_fsmevent);
    }

}