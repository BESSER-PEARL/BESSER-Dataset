





import java.util.List;
import java.util.ArrayList;

public class Statecharts_StateVertex  {






    private List<Transition> transitions;




    private List<Transition> transitions;


    public Statecharts_StateVertex(
    ) {
        this.transitions = new ArrayList<>();
        this.transitions = new ArrayList<>();
    }

    public Statecharts_StateVertex(
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

}