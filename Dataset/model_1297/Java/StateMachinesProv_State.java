





import java.util.List;
import java.util.ArrayList;

public class StateMachinesProv_State extends Vertex {

    private boolean isComposite;
    private boolean isOrthogonal;
    private boolean isSubmachineState;
    private boolean isSimple;





    private List<StateMachinesProv_Pseudostate> statemachinesprov_pseudostates;




    private List<StateMachinesProv_Region> statemachinesprov_regions;




    private StateMachinesProv_Pseudostate statemachinesprov_pseudostate;




    private StateMachinesProv_StateMachine statemachinesprov_statemachine;




    private StateMachinesProv_State statemachinesprov_state;




    private StateMachinesProv_Region statemachinesprov_region;




    private StateMachinesProv_StateMachine statemachinesprov_statemachine;


    public StateMachinesProv_State(
        boolean isComposite,        boolean isOrthogonal,        boolean isSubmachineState,        boolean isSimple    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isOrthogonal = isOrthogonal;
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
        this.statemachinesprov_pseudostates = new ArrayList<>();
        this.statemachinesprov_regions = new ArrayList<>();
    }

    public StateMachinesProv_State(
        boolean isComposite,        boolean isOrthogonal,        boolean isSubmachineState,        boolean isSimple        ArrayList<StateMachinesProv_Pseudostate> statemachinesprov_pseudostates,        ArrayList<StateMachinesProv_Region> statemachinesprov_regions    ) {
        this.isComposite = isComposite;
        this.isOrthogonal = isOrthogonal;
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
        this.statemachinesprov_pseudostates = statemachinesprov_pseudostates;
        this.statemachinesprov_regions = statemachinesprov_regions;
    }

    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public boolean getIsorthogonal() {
        return isOrthogonal;
    }

    public void setIsorthogonal(boolean isOrthogonal) {
        this.isOrthogonal = isOrthogonal;
    }
    public boolean getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(boolean isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
    }
    public boolean getIssimple() {
        return isSimple;
    }

    public void setIssimple(boolean isSimple) {
        this.isSimple = isSimple;
    }

    public List<StateMachinesProv_Pseudostate> getStatemachinesprov_pseudostates() {
        return statemachinesprov_pseudostates;
    }

    public void addStatemachinesprov_pseudostate(Statemachinesprov_pseudostate statemachinesprov_pseudostate) {
        this.statemachinesprov_pseudostates.add(statemachinesprov_pseudostate);
    }
    public List<StateMachinesProv_Region> getStatemachinesprov_regions() {
        return statemachinesprov_regions;
    }

    public void addStatemachinesprov_region(Statemachinesprov_region statemachinesprov_region) {
        this.statemachinesprov_regions.add(statemachinesprov_region);
    }
    public StateMachinesProv_Pseudostate getStatemachinesprov_pseudostate() {
        return statemachinesprov_pseudostate;
    }

    public void setStatemachinesprov_pseudostate(StateMachinesProv_Pseudostate statemachinesprov_pseudostate) {
        this.statemachinesprov_pseudostate = statemachinesprov_pseudostate;
    }
    public StateMachinesProv_StateMachine getStatemachinesprov_statemachine() {
        return statemachinesprov_statemachine;
    }

    public void setStatemachinesprov_statemachine(StateMachinesProv_StateMachine statemachinesprov_statemachine) {
        this.statemachinesprov_statemachine = statemachinesprov_statemachine;
    }
    public StateMachinesProv_State getStatemachinesprov_state() {
        return statemachinesprov_state;
    }

    public void setStatemachinesprov_state(StateMachinesProv_State statemachinesprov_state) {
        this.statemachinesprov_state = statemachinesprov_state;
    }
    public StateMachinesProv_Region getStatemachinesprov_region() {
        return statemachinesprov_region;
    }

    public void setStatemachinesprov_region(StateMachinesProv_Region statemachinesprov_region) {
        this.statemachinesprov_region = statemachinesprov_region;
    }
    public StateMachinesProv_StateMachine getStatemachinesprov_statemachine() {
        return statemachinesprov_statemachine;
    }

    public void setStatemachinesprov_statemachine(StateMachinesProv_StateMachine statemachinesprov_statemachine) {
        this.statemachinesprov_statemachine = statemachinesprov_statemachine;
    }

}