





import java.util.List;
import java.util.ArrayList;

public class fsml_FSMState  {

    private String name;
    private boolean initial;





    private fsml_FSMTransition fsml_fsmtransition;




    private fsml_FSM fsml_fsm;




    private List<fsml_FSMTransition> fsml_fsmtransitions;


    public fsml_FSMState(
        String name,        boolean initial    ) {
        this.name = name;
        this.initial = initial;
        this.fsml_fsmtransitions = new ArrayList<>();
    }

    public fsml_FSMState(
        String name,        boolean initial        ArrayList<fsml_FSMTransition> fsml_fsmtransitions    ) {
        this.name = name;
        this.initial = initial;
        this.fsml_fsmtransitions = fsml_fsmtransitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public fsml_FSMTransition getFsml_fsmtransition() {
        return fsml_fsmtransition;
    }

    public void setFsml_fsmtransition(fsml_FSMTransition fsml_fsmtransition) {
        this.fsml_fsmtransition = fsml_fsmtransition;
    }
    public fsml_FSM getFsml_fsm() {
        return fsml_fsm;
    }

    public void setFsml_fsm(fsml_FSM fsml_fsm) {
        this.fsml_fsm = fsml_fsm;
    }
    public List<fsml_FSMTransition> getFsml_fsmtransitions() {
        return fsml_fsmtransitions;
    }

    public void addFsml_fsmtransition(Fsml_fsmtransition fsml_fsmtransition) {
        this.fsml_fsmtransitions.add(fsml_fsmtransition);
    }

}