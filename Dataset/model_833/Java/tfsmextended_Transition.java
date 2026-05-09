





import java.util.List;
import java.util.ArrayList;

public class tfsmextended_Transition extends NamedElement {

    private String action;





    private tfsmextended_State tfsmextended_state;




    private tfsmextended_FSMEvent tfsmextended_fsmevent;




    private tfsmextended_State tfsmextended_state;




    private tfsmextended_State tfsmextended_state;




    private List<tfsmextended_FSMEvent> tfsmextended_fsmevents;




    private tfsmextended_Guard tfsmextended_guard;




    private tfsmextended_TFSM tfsmextended_tfsm;




    private tfsmextended_State tfsmextended_state;


    public tfsmextended_Transition(
        String action    ) {
        super(
        );
        this.action = action;
        this.tfsmextended_fsmevents = new ArrayList<>();
    }

    public tfsmextended_Transition(
        String action        ArrayList<tfsmextended_FSMEvent> tfsmextended_fsmevents    ) {
        this.action = action;
        this.tfsmextended_fsmevents = tfsmextended_fsmevents;
    }

    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public tfsmextended_State getTfsmextended_state() {
        return tfsmextended_state;
    }

    public void setTfsmextended_state(tfsmextended_State tfsmextended_state) {
        this.tfsmextended_state = tfsmextended_state;
    }
    public tfsmextended_FSMEvent getTfsmextended_fsmevent() {
        return tfsmextended_fsmevent;
    }

    public void setTfsmextended_fsmevent(tfsmextended_FSMEvent tfsmextended_fsmevent) {
        this.tfsmextended_fsmevent = tfsmextended_fsmevent;
    }
    public tfsmextended_State getTfsmextended_state() {
        return tfsmextended_state;
    }

    public void setTfsmextended_state(tfsmextended_State tfsmextended_state) {
        this.tfsmextended_state = tfsmextended_state;
    }
    public tfsmextended_State getTfsmextended_state() {
        return tfsmextended_state;
    }

    public void setTfsmextended_state(tfsmextended_State tfsmextended_state) {
        this.tfsmextended_state = tfsmextended_state;
    }
    public List<tfsmextended_FSMEvent> getTfsmextended_fsmevents() {
        return tfsmextended_fsmevents;
    }

    public void addTfsmextended_fsmevent(Tfsmextended_fsmevent tfsmextended_fsmevent) {
        this.tfsmextended_fsmevents.add(tfsmextended_fsmevent);
    }
    public tfsmextended_Guard getTfsmextended_guard() {
        return tfsmextended_guard;
    }

    public void setTfsmextended_guard(tfsmextended_Guard tfsmextended_guard) {
        this.tfsmextended_guard = tfsmextended_guard;
    }
    public tfsmextended_TFSM getTfsmextended_tfsm() {
        return tfsmextended_tfsm;
    }

    public void setTfsmextended_tfsm(tfsmextended_TFSM tfsmextended_tfsm) {
        this.tfsmextended_tfsm = tfsmextended_tfsm;
    }
    public tfsmextended_State getTfsmextended_state() {
        return tfsmextended_state;
    }

    public void setTfsmextended_state(tfsmextended_State tfsmextended_state) {
        this.tfsmextended_state = tfsmextended_state;
    }

}