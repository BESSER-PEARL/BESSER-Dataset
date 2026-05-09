





import java.util.List;
import java.util.ArrayList;

public class fsm_Buffer extends NamedElement {

    private String currentValues;
    private String initialValue;





    private List<fsm_StateMachine> fsm_statemachines;




    private List<fsm_StateMachine> fsm_statemachines;


    public fsm_Buffer(
        String currentValues,        String initialValue    ) {
        super(
        );
        this.currentValues = currentValues;
        this.initialValue = initialValue;
        this.fsm_statemachines = new ArrayList<>();
        this.fsm_statemachines = new ArrayList<>();
    }

    public fsm_Buffer(
        String currentValues,        String initialValue        ArrayList<fsm_StateMachine> fsm_statemachines,        ArrayList<fsm_StateMachine> fsm_statemachines    ) {
        this.currentValues = currentValues;
        this.initialValue = initialValue;
        this.fsm_statemachines = fsm_statemachines;
        this.fsm_statemachines = fsm_statemachines;
    }

    public String getCurrentvalues() {
        return currentValues;
    }

    public void setCurrentvalues(String currentValues) {
        this.currentValues = currentValues;
    }
    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }

    public List<fsm_StateMachine> getFsm_statemachines() {
        return fsm_statemachines;
    }

    public void addFsm_statemachine(Fsm_statemachine fsm_statemachine) {
        this.fsm_statemachines.add(fsm_statemachine);
    }
    public List<fsm_StateMachine> getFsm_statemachines() {
        return fsm_statemachines;
    }

    public void addFsm_statemachine(Fsm_statemachine fsm_statemachine) {
        this.fsm_statemachines.add(fsm_statemachine);
    }

}