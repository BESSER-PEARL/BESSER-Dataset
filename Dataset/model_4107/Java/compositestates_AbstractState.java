





import java.util.List;
import java.util.ArrayList;

public class compositestates_AbstractState  {






    private compositestates_Transition compositestates_transition;




    private List<compositestates_Transition> compositestates_transitions;




    private List<compositestates_Transition> compositestates_transitions;




    private compositestates_Region compositestates_region;




    private compositestates_Transition compositestates_transition;




    private compositestates_Region compositestates_region;


    public compositestates_AbstractState(
    ) {
        this.compositestates_transitions = new ArrayList<>();
        this.compositestates_transitions = new ArrayList<>();
    }

    public compositestates_AbstractState(
        ArrayList<compositestates_Transition> compositestates_transitions,        ArrayList<compositestates_Transition> compositestates_transitions    ) {
        this.compositestates_transitions = compositestates_transitions;
        this.compositestates_transitions = compositestates_transitions;
    }


    public compositestates_Transition getCompositestates_transition() {
        return compositestates_transition;
    }

    public void setCompositestates_transition(compositestates_Transition compositestates_transition) {
        this.compositestates_transition = compositestates_transition;
    }
    public List<compositestates_Transition> getCompositestates_transitions() {
        return compositestates_transitions;
    }

    public void addCompositestates_transition(Compositestates_transition compositestates_transition) {
        this.compositestates_transitions.add(compositestates_transition);
    }
    public List<compositestates_Transition> getCompositestates_transitions() {
        return compositestates_transitions;
    }

    public void addCompositestates_transition(Compositestates_transition compositestates_transition) {
        this.compositestates_transitions.add(compositestates_transition);
    }
    public compositestates_Region getCompositestates_region() {
        return compositestates_region;
    }

    public void setCompositestates_region(compositestates_Region compositestates_region) {
        this.compositestates_region = compositestates_region;
    }
    public compositestates_Transition getCompositestates_transition() {
        return compositestates_transition;
    }

    public void setCompositestates_transition(compositestates_Transition compositestates_transition) {
        this.compositestates_transition = compositestates_transition;
    }
    public compositestates_Region getCompositestates_region() {
        return compositestates_region;
    }

    public void setCompositestates_region(compositestates_Region compositestates_region) {
        this.compositestates_region = compositestates_region;
    }

}