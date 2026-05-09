





import java.util.List;
import java.util.ArrayList;

public class statesml_Node  {

    private String name;





    private statesml_Transition statesml_transition;




    private statesml_StatesMLModel statesml_statesmlmodel;




    private List<statesml_Transition> statesml_transitions;


    public statesml_Node(
        String name    ) {
        this.name = name;
        this.statesml_transitions = new ArrayList<>();
    }

    public statesml_Node(
        String name        ArrayList<statesml_Transition> statesml_transitions    ) {
        this.name = name;
        this.statesml_transitions = statesml_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statesml_Transition getStatesml_transition() {
        return statesml_transition;
    }

    public void setStatesml_transition(statesml_Transition statesml_transition) {
        this.statesml_transition = statesml_transition;
    }
    public statesml_StatesMLModel getStatesml_statesmlmodel() {
        return statesml_statesmlmodel;
    }

    public void setStatesml_statesmlmodel(statesml_StatesMLModel statesml_statesmlmodel) {
        this.statesml_statesmlmodel = statesml_statesmlmodel;
    }
    public List<statesml_Transition> getStatesml_transitions() {
        return statesml_transitions;
    }

    public void addStatesml_transition(Statesml_transition statesml_transition) {
        this.statesml_transitions.add(statesml_transition);
    }

}