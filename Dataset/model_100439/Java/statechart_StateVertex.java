





import java.util.List;
import java.util.ArrayList;

public class statechart_StateVertex extends NameBase, IDBase {






    private statechart_Transition statechart_transition;




    private statechart_Transition statechart_transition;




    private List<statechart_Transition> statechart_transitions;




    private List<statechart_Label> statechart_labels;




    private List<statechart_Transition> statechart_transitions;


    public statechart_StateVertex(
    ) {
        super(
        );
        this.statechart_transitions = new ArrayList<>();
        this.statechart_labels = new ArrayList<>();
        this.statechart_transitions = new ArrayList<>();
    }

    public statechart_StateVertex(
        ArrayList<statechart_Transition> statechart_transitions,        ArrayList<statechart_Label> statechart_labels,        ArrayList<statechart_Transition> statechart_transitions    ) {
        this.statechart_transitions = statechart_transitions;
        this.statechart_labels = statechart_labels;
        this.statechart_transitions = statechart_transitions;
    }


    public statechart_Transition getStatechart_transition() {
        return statechart_transition;
    }

    public void setStatechart_transition(statechart_Transition statechart_transition) {
        this.statechart_transition = statechart_transition;
    }
    public statechart_Transition getStatechart_transition() {
        return statechart_transition;
    }

    public void setStatechart_transition(statechart_Transition statechart_transition) {
        this.statechart_transition = statechart_transition;
    }
    public List<statechart_Transition> getStatechart_transitions() {
        return statechart_transitions;
    }

    public void addStatechart_transition(Statechart_transition statechart_transition) {
        this.statechart_transitions.add(statechart_transition);
    }
    public List<statechart_Label> getStatechart_labels() {
        return statechart_labels;
    }

    public void addStatechart_label(Statechart_label statechart_label) {
        this.statechart_labels.add(statechart_label);
    }
    public List<statechart_Transition> getStatechart_transitions() {
        return statechart_transitions;
    }

    public void addStatechart_transition(Statechart_transition statechart_transition) {
        this.statechart_transitions.add(statechart_transition);
    }

}