





import java.util.List;
import java.util.ArrayList;

public class sgraph_Vertex extends NamedElement {






    private sgraph_Transition sgraph_transition;




    private List<sgraph_Transition> sgraph_transitions;




    private List<sgraph_Transition> sgraph_transitions;




    private sgraph_Transition sgraph_transition;


    public sgraph_Vertex(
    ) {
        super(
        );
        this.sgraph_transitions = new ArrayList<>();
        this.sgraph_transitions = new ArrayList<>();
    }

    public sgraph_Vertex(
        ArrayList<sgraph_Transition> sgraph_transitions,        ArrayList<sgraph_Transition> sgraph_transitions    ) {
        this.sgraph_transitions = sgraph_transitions;
        this.sgraph_transitions = sgraph_transitions;
    }


    public sgraph_Transition getSgraph_transition() {
        return sgraph_transition;
    }

    public void setSgraph_transition(sgraph_Transition sgraph_transition) {
        this.sgraph_transition = sgraph_transition;
    }
    public List<sgraph_Transition> getSgraph_transitions() {
        return sgraph_transitions;
    }

    public void addSgraph_transition(Sgraph_transition sgraph_transition) {
        this.sgraph_transitions.add(sgraph_transition);
    }
    public List<sgraph_Transition> getSgraph_transitions() {
        return sgraph_transitions;
    }

    public void addSgraph_transition(Sgraph_transition sgraph_transition) {
        this.sgraph_transitions.add(sgraph_transition);
    }
    public sgraph_Transition getSgraph_transition() {
        return sgraph_transition;
    }

    public void setSgraph_transition(sgraph_Transition sgraph_transition) {
        this.sgraph_transition = sgraph_transition;
    }

}