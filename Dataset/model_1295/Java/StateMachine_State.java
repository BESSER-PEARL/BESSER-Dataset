





import java.util.List;
import java.util.ArrayList;

public class StateMachine_State extends Vertex {

    private String isSubmachineState;
    private String isSimple;
    private String isComposite;





    private List<StateMachine_PseudoState> statemachine_pseudostates;




    private StateMachine_StateMachine statemachine_statemachine;




    private StateMachine_PseudoState statemachine_pseudostate;




    private StateMachine_StateMachine statemachine_statemachine;




    private StateMachine_Constraint statemachine_constraint;


    public StateMachine_State(
        String isSubmachineState,        String isSimple,        String isComposite    ) {
        super(
        );
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
        this.isComposite = isComposite;
        this.statemachine_pseudostates = new ArrayList<>();
    }

    public StateMachine_State(
        String isSubmachineState,        String isSimple,        String isComposite        ArrayList<StateMachine_PseudoState> statemachine_pseudostates    ) {
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
        this.isComposite = isComposite;
        this.statemachine_pseudostates = statemachine_pseudostates;
    }

    public String getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(String isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
    }
    public String getIssimple() {
        return isSimple;
    }

    public void setIssimple(String isSimple) {
        this.isSimple = isSimple;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }

    public List<StateMachine_PseudoState> getStatemachine_pseudostates() {
        return statemachine_pseudostates;
    }

    public void addStatemachine_pseudostate(Statemachine_pseudostate statemachine_pseudostate) {
        this.statemachine_pseudostates.add(statemachine_pseudostate);
    }
    public StateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(StateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public StateMachine_PseudoState getStatemachine_pseudostate() {
        return statemachine_pseudostate;
    }

    public void setStatemachine_pseudostate(StateMachine_PseudoState statemachine_pseudostate) {
        this.statemachine_pseudostate = statemachine_pseudostate;
    }
    public StateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(StateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public StateMachine_Constraint getStatemachine_constraint() {
        return statemachine_constraint;
    }

    public void setStatemachine_constraint(StateMachine_Constraint statemachine_constraint) {
        this.statemachine_constraint = statemachine_constraint;
    }

}