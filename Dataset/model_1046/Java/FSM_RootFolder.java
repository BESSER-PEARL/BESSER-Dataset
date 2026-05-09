





import java.util.List;
import java.util.ArrayList;

public class FSM_RootFolder  {

    private String name;





    private FSM_StateMachine fsm_statemachine;




    private List<FSM_StateMachine> fsm_statemachines;




    private FSM_RootFolder fsm_rootfolder;


    public FSM_RootFolder(
        String name    ) {
        this.name = name;
        this.fsm_statemachines = new ArrayList<>();
    }

    public FSM_RootFolder(
        String name        ArrayList<FSM_StateMachine> fsm_statemachines    ) {
        this.name = name;
        this.fsm_statemachines = fsm_statemachines;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FSM_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(FSM_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }
    public List<FSM_StateMachine> getFsm_statemachines() {
        return fsm_statemachines;
    }

    public void addFsm_statemachine(Fsm_statemachine fsm_statemachine) {
        this.fsm_statemachines.add(fsm_statemachine);
    }
    public FSM_RootFolder getFsm_rootfolder() {
        return fsm_rootfolder;
    }

    public void setFsm_rootfolder(FSM_RootFolder fsm_rootfolder) {
        this.fsm_rootfolder = fsm_rootfolder;
    }

}