





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition  {

    private String name;
    private boolean InverseGuard;





    private fsm_Guard fsm_guard;




    private fsm_State fsm_state;




    private fsm_Event fsm_event;




    private fsm_State fsm_state;




    private List<fsm_Action> fsm_actions;




    private fsm_State fsm_state;




    private fsm_State fsm_state;


    public fsm_Transition(
        String name,        boolean InverseGuard    ) {
        this.name = name;
        this.InverseGuard = InverseGuard;
        this.fsm_actions = new ArrayList<>();
    }

    public fsm_Transition(
        String name,        boolean InverseGuard        ArrayList<fsm_Action> fsm_actions    ) {
        this.name = name;
        this.InverseGuard = InverseGuard;
        this.fsm_actions = fsm_actions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getInverseguard() {
        return InverseGuard;
    }

    public void setInverseguard(boolean InverseGuard) {
        this.InverseGuard = InverseGuard;
    }

    public fsm_Guard getFsm_guard() {
        return fsm_guard;
    }

    public void setFsm_guard(fsm_Guard fsm_guard) {
        this.fsm_guard = fsm_guard;
    }
    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public fsm_Event getFsm_event() {
        return fsm_event;
    }

    public void setFsm_event(fsm_Event fsm_event) {
        this.fsm_event = fsm_event;
    }
    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public List<fsm_Action> getFsm_actions() {
        return fsm_actions;
    }

    public void addFsm_action(Fsm_action fsm_action) {
        this.fsm_actions.add(fsm_action);
    }
    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }

}