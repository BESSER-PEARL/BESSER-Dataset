





import java.util.List;
import java.util.ArrayList;

public class model_State  {

    private String name;





    private model_FSM model_fsm;




    private model_FSM model_fsm;




    private model_Transition model_transition;




    private List<model_Transition> model_transitions;




    private model_Transition model_transition;




    private model_FSM model_fsm;




    private List<model_Transition> model_transitions;


    public model_State(
        String name    ) {
        this.name = name;
        this.model_transitions = new ArrayList<>();
        this.model_transitions = new ArrayList<>();
    }

    public model_State(
        String name        ArrayList<model_Transition> model_transitions,        ArrayList<model_Transition> model_transitions    ) {
        this.name = name;
        this.model_transitions = model_transitions;
        this.model_transitions = model_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_FSM getModel_fsm() {
        return model_fsm;
    }

    public void setModel_fsm(model_FSM model_fsm) {
        this.model_fsm = model_fsm;
    }
    public model_FSM getModel_fsm() {
        return model_fsm;
    }

    public void setModel_fsm(model_FSM model_fsm) {
        this.model_fsm = model_fsm;
    }
    public model_Transition getModel_transition() {
        return model_transition;
    }

    public void setModel_transition(model_Transition model_transition) {
        this.model_transition = model_transition;
    }
    public List<model_Transition> getModel_transitions() {
        return model_transitions;
    }

    public void addModel_transition(Model_transition model_transition) {
        this.model_transitions.add(model_transition);
    }
    public model_Transition getModel_transition() {
        return model_transition;
    }

    public void setModel_transition(model_Transition model_transition) {
        this.model_transition = model_transition;
    }
    public model_FSM getModel_fsm() {
        return model_fsm;
    }

    public void setModel_fsm(model_FSM model_fsm) {
        this.model_fsm = model_fsm;
    }
    public List<model_Transition> getModel_transitions() {
        return model_transitions;
    }

    public void addModel_transition(Model_transition model_transition) {
        this.model_transitions.add(model_transition);
    }

}