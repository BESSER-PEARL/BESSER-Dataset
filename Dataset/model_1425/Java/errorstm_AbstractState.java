





import java.util.List;
import java.util.ArrayList;

public class errorstm_AbstractState  {

    private String name;





    private List<errorstm_Transition> errorstm_transitions;




    private errorstm_Transition errorstm_transition;




    private List<errorstm_Transition> errorstm_transitions;




    private errorstm_Transition errorstm_transition;


    public errorstm_AbstractState(
        String name    ) {
        this.name = name;
        this.errorstm_transitions = new ArrayList<>();
        this.errorstm_transitions = new ArrayList<>();
    }

    public errorstm_AbstractState(
        String name        ArrayList<errorstm_Transition> errorstm_transitions,        ArrayList<errorstm_Transition> errorstm_transitions    ) {
        this.name = name;
        this.errorstm_transitions = errorstm_transitions;
        this.errorstm_transitions = errorstm_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<errorstm_Transition> getErrorstm_transitions() {
        return errorstm_transitions;
    }

    public void addErrorstm_transition(Errorstm_transition errorstm_transition) {
        this.errorstm_transitions.add(errorstm_transition);
    }
    public errorstm_Transition getErrorstm_transition() {
        return errorstm_transition;
    }

    public void setErrorstm_transition(errorstm_Transition errorstm_transition) {
        this.errorstm_transition = errorstm_transition;
    }
    public List<errorstm_Transition> getErrorstm_transitions() {
        return errorstm_transitions;
    }

    public void addErrorstm_transition(Errorstm_transition errorstm_transition) {
        this.errorstm_transitions.add(errorstm_transition);
    }
    public errorstm_Transition getErrorstm_transition() {
        return errorstm_transition;
    }

    public void setErrorstm_transition(errorstm_Transition errorstm_transition) {
        this.errorstm_transition = errorstm_transition;
    }

}