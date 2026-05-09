





import java.util.List;
import java.util.ArrayList;

public class FSM_FStateMachine  {

    private String name;





    private FSM_FAbstractState fsm_fabstractstate;




    private List<FSM_FAbstractState> fsm_fabstractstates;


    public FSM_FStateMachine(
        String name    ) {
        this.name = name;
        this.fsm_fabstractstates = new ArrayList<>();
    }

    public FSM_FStateMachine(
        String name        ArrayList<FSM_FAbstractState> fsm_fabstractstates    ) {
        this.name = name;
        this.fsm_fabstractstates = fsm_fabstractstates;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FSM_FAbstractState getFsm_fabstractstate() {
        return fsm_fabstractstate;
    }

    public void setFsm_fabstractstate(FSM_FAbstractState fsm_fabstractstate) {
        this.fsm_fabstractstate = fsm_fabstractstate;
    }
    public List<FSM_FAbstractState> getFsm_fabstractstates() {
        return fsm_fabstractstates;
    }

    public void addFsm_fabstractstate(Fsm_fabstractstate fsm_fabstractstate) {
        this.fsm_fabstractstates.add(fsm_fabstractstate);
    }

}