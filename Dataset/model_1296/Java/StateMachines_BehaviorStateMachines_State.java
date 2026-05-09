





import java.util.List;
import java.util.ArrayList;

public class StateMachines_BehaviorStateMachines_State extends BehaviorStateMachines_Namespace, BehaviorStateMachines_RedefinableElement, BehaviorStateMachines_Vertex {

    private boolean isSimple;
    private boolean isOrthogonal;
    private boolean isComposite;
    private boolean isSubmachineState;





    private Constraint constraint;




    private State state;




    private StateMachine statemachine;




    private List<Region> regions;




    private Behavior behavior;




    private List<Trigger> triggers;




    private List<Pseudostate> pseudostates;




    private Behavior behavior;




    private Behavior behavior;


    public StateMachines_BehaviorStateMachines_State(
        boolean isSimple,        boolean isOrthogonal,        boolean isComposite,        boolean isSubmachineState    ) {
        super(
        );
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.isComposite = isComposite;
        this.isSubmachineState = isSubmachineState;
        this.regions = new ArrayList<>();
        this.triggers = new ArrayList<>();
        this.pseudostates = new ArrayList<>();
    }

    public StateMachines_BehaviorStateMachines_State(
        boolean isSimple,        boolean isOrthogonal,        boolean isComposite,        boolean isSubmachineState        ArrayList<Region> regions,        ArrayList<Trigger> triggers,        ArrayList<Pseudostate> pseudostates    ) {
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.isComposite = isComposite;
        this.isSubmachineState = isSubmachineState;
        this.regions = regions;
        this.triggers = triggers;
        this.pseudostates = pseudostates;
    }

    public boolean getIssimple() {
        return isSimple;
    }

    public void setIssimple(boolean isSimple) {
        this.isSimple = isSimple;
    }
    public boolean getIsorthogonal() {
        return isOrthogonal;
    }

    public void setIsorthogonal(boolean isOrthogonal) {
        this.isOrthogonal = isOrthogonal;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public boolean getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(boolean isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
    }

    public Constraint getConstraint() {
        return constraint;
    }

    public void setConstraint(Constraint constraint) {
        this.constraint = constraint;
    }
    public State getState() {
        return state;
    }

    public void setState(State state) {
        this.state = state;
    }
    public StateMachine getStatemachine() {
        return statemachine;
    }

    public void setStatemachine(StateMachine statemachine) {
        this.statemachine = statemachine;
    }
    public List<Region> getRegions() {
        return regions;
    }

    public void addRegion(Region region) {
        this.regions.add(region);
    }
    public Behavior getBehavior() {
        return behavior;
    }

    public void setBehavior(Behavior behavior) {
        this.behavior = behavior;
    }
    public List<Trigger> getTriggers() {
        return triggers;
    }

    public void addTrigger(Trigger trigger) {
        this.triggers.add(trigger);
    }
    public List<Pseudostate> getPseudostates() {
        return pseudostates;
    }

    public void addPseudostate(Pseudostate pseudostate) {
        this.pseudostates.add(pseudostate);
    }
    public Behavior getBehavior() {
        return behavior;
    }

    public void setBehavior(Behavior behavior) {
        this.behavior = behavior;
    }
    public Behavior getBehavior() {
        return behavior;
    }

    public void setBehavior(Behavior behavior) {
        this.behavior = behavior;
    }

}