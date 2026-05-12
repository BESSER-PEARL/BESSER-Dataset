





import java.util.List;
import java.util.ArrayList;

public class Statecharts_State extends StateVertex {






    private List<Transition> transitions;


    public Statecharts_State(
    ) {
        super(
        );
        this.transitions = new ArrayList<>();
    }

    public Statecharts_State(
        ArrayList<Transition> transitions    ) {
        this.transitions = transitions;
    }


    public List<Transition> getTransitions() {
        return transitions;
    }

    public void addTransition(Transition transition) {
        this.transitions.add(transition);
    }

}