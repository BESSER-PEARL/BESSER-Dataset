





import java.util.List;
import java.util.ArrayList;

public class PathExp_State  {






    private List<Transition> transitions;




    private List<Transition> transitions;




    private PathExp pathexp;


    public PathExp_State(
    ) {
        this.transitions = new ArrayList<>();
        this.transitions = new ArrayList<>();
    }

    public PathExp_State(
        ArrayList<Transition> transitions,        ArrayList<Transition> transitions    ) {
        this.transitions = transitions;
        this.transitions = transitions;
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
    public PathExp getPathexp() {
        return pathexp;
    }

    public void setPathexp(PathExp pathexp) {
        this.pathexp = pathexp;
    }

}