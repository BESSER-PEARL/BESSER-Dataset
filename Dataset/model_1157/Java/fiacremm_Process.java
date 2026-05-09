





import java.util.List;
import java.util.ArrayList;

public class fiacremm_Process extends EModelElement {

    private int StateSize;
    private int VarSize;
    private String Name;





    private List<fiacremm_Transition> fiacremm_transitions;




    private List<fiacremm_State> fiacremm_states;




    private fiacremm_State fiacremm_state;




    private fiacremm_State fiacremm_state;




    private List<fiacremm_Trigger> fiacremm_triggers;




    private fiacremm_Port fiacremm_port;




    private fiacremm_Variable fiacremm_variable;




    private List<fiacremm_Variable> fiacremm_variables;


    public fiacremm_Process(
        int StateSize,        int VarSize,        String Name    ) {
        super(
        );
        this.StateSize = StateSize;
        this.VarSize = VarSize;
        this.Name = Name;
        this.fiacremm_transitions = new ArrayList<>();
        this.fiacremm_states = new ArrayList<>();
        this.fiacremm_triggers = new ArrayList<>();
        this.fiacremm_variables = new ArrayList<>();
    }

    public fiacremm_Process(
        int StateSize,        int VarSize,        String Name        ArrayList<fiacremm_Transition> fiacremm_transitions,        ArrayList<fiacremm_State> fiacremm_states,        ArrayList<fiacremm_Trigger> fiacremm_triggers,        ArrayList<fiacremm_Variable> fiacremm_variables    ) {
        this.StateSize = StateSize;
        this.VarSize = VarSize;
        this.Name = Name;
        this.fiacremm_transitions = fiacremm_transitions;
        this.fiacremm_states = fiacremm_states;
        this.fiacremm_triggers = fiacremm_triggers;
        this.fiacremm_variables = fiacremm_variables;
    }

    public int getStatesize() {
        return StateSize;
    }

    public void setStatesize(int StateSize) {
        this.StateSize = StateSize;
    }
    public int getVarsize() {
        return VarSize;
    }

    public void setVarsize(int VarSize) {
        this.VarSize = VarSize;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<fiacremm_Transition> getFiacremm_transitions() {
        return fiacremm_transitions;
    }

    public void addFiacremm_transition(Fiacremm_transition fiacremm_transition) {
        this.fiacremm_transitions.add(fiacremm_transition);
    }
    public List<fiacremm_State> getFiacremm_states() {
        return fiacremm_states;
    }

    public void addFiacremm_state(Fiacremm_state fiacremm_state) {
        this.fiacremm_states.add(fiacremm_state);
    }
    public fiacremm_State getFiacremm_state() {
        return fiacremm_state;
    }

    public void setFiacremm_state(fiacremm_State fiacremm_state) {
        this.fiacremm_state = fiacremm_state;
    }
    public fiacremm_State getFiacremm_state() {
        return fiacremm_state;
    }

    public void setFiacremm_state(fiacremm_State fiacremm_state) {
        this.fiacremm_state = fiacremm_state;
    }
    public List<fiacremm_Trigger> getFiacremm_triggers() {
        return fiacremm_triggers;
    }

    public void addFiacremm_trigger(Fiacremm_trigger fiacremm_trigger) {
        this.fiacremm_triggers.add(fiacremm_trigger);
    }
    public fiacremm_Port getFiacremm_port() {
        return fiacremm_port;
    }

    public void setFiacremm_port(fiacremm_Port fiacremm_port) {
        this.fiacremm_port = fiacremm_port;
    }
    public fiacremm_Variable getFiacremm_variable() {
        return fiacremm_variable;
    }

    public void setFiacremm_variable(fiacremm_Variable fiacremm_variable) {
        this.fiacremm_variable = fiacremm_variable;
    }
    public List<fiacremm_Variable> getFiacremm_variables() {
        return fiacremm_variables;
    }

    public void addFiacremm_variable(Fiacremm_variable fiacremm_variable) {
        this.fiacremm_variables.add(fiacremm_variable);
    }

}