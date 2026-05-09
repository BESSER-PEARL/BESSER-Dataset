





import java.util.List;
import java.util.ArrayList;

public class StateMachines_BehaviorStateMachines_Region extends BehaviorStateMachines_Namespace, BehaviorStateMachines_RedefinableElement {






    private Region region;




    private State state;




    private StateMachine statemachine;


    public StateMachines_BehaviorStateMachines_Region(
    ) {
        super(
        );
    }



    public Region getRegion() {
        return region;
    }

    public void setRegion(Region region) {
        this.region = region;
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

}