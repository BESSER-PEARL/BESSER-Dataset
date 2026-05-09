





import java.util.List;
import java.util.ArrayList;

public class statechart_AbstractState extends ModelElement {






    private List<statechart_Transition> statechart_transitions;




    private List<statechart_Transition> statechart_transitions;




    private List<statechart_Action> statechart_actions;




    private statechart_Transition statechart_transition;




    private statechart_CompositeState statechart_compositestate;




    private statechart_Transition statechart_transition;


    public statechart_AbstractState(
    ) {
        super(
        );
        this.statechart_transitions = new ArrayList<>();
        this.statechart_transitions = new ArrayList<>();
        this.statechart_actions = new ArrayList<>();
    }

    public statechart_AbstractState(
        ArrayList<statechart_Transition> statechart_transitions,        ArrayList<statechart_Transition> statechart_transitions,        ArrayList<statechart_Action> statechart_actions    ) {
        this.statechart_transitions = statechart_transitions;
        this.statechart_transitions = statechart_transitions;
        this.statechart_actions = statechart_actions;
    }


    public List<statechart_Transition> getStatechart_transitions() {
        return statechart_transitions;
    }

    public void addStatechart_transition(Statechart_transition statechart_transition) {
        this.statechart_transitions.add(statechart_transition);
    }
    public List<statechart_Transition> getStatechart_transitions() {
        return statechart_transitions;
    }

    public void addStatechart_transition(Statechart_transition statechart_transition) {
        this.statechart_transitions.add(statechart_transition);
    }
    public List<statechart_Action> getStatechart_actions() {
        return statechart_actions;
    }

    public void addStatechart_action(Statechart_action statechart_action) {
        this.statechart_actions.add(statechart_action);
    }
    public statechart_Transition getStatechart_transition() {
        return statechart_transition;
    }

    public void setStatechart_transition(statechart_Transition statechart_transition) {
        this.statechart_transition = statechart_transition;
    }
    public statechart_CompositeState getStatechart_compositestate() {
        return statechart_compositestate;
    }

    public void setStatechart_compositestate(statechart_CompositeState statechart_compositestate) {
        this.statechart_compositestate = statechart_compositestate;
    }
    public statechart_Transition getStatechart_transition() {
        return statechart_transition;
    }

    public void setStatechart_transition(statechart_Transition statechart_transition) {
        this.statechart_transition = statechart_transition;
    }

}