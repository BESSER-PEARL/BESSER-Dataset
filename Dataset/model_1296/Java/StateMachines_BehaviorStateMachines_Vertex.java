





import java.util.List;
import java.util.ArrayList;

public class StateMachines_BehaviorStateMachines_Vertex extends NamedElement {






    private Region region;




    private List<Transition> transitions;




    private List<Transition> transitions;


    public StateMachines_BehaviorStateMachines_Vertex(
    ) {
        super(
        );
        this.transitions = new ArrayList<>();
        this.transitions = new ArrayList<>();
    }

    public StateMachines_BehaviorStateMachines_Vertex(
        ArrayList<Transition> transitions,        ArrayList<Transition> transitions    ) {
        this.transitions = transitions;
        this.transitions = transitions;
    }


    public Region getRegion() {
        return region;
    }

    public void setRegion(Region region) {
        this.region = region;
    }
    public List<Transition> getTransitions() {
        return transitions;
    }

    public void addTransition(Transition transition) {
        this.transitions.add(transition);
    }
    public List<Transition> getTransitions() {
        return transitions;
    }

    public void addTransition(Transition transition) {
        this.transitions.add(transition);
    }

}