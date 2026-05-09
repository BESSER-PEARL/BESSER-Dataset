





import java.util.List;
import java.util.ArrayList;

public class statemachine_State  {

    private String name;





    private statemachine_Statemachine statemachine_statemachine;




    private List<statemachine_Command> statemachine_commands;




    private statemachine_Transition statemachine_transition;




    private List<statemachine_Transition> statemachine_transitions;


    public statemachine_State(
        String name    ) {
        this.name = name;
        this.statemachine_commands = new ArrayList<>();
        this.statemachine_transitions = new ArrayList<>();
    }

    public statemachine_State(
        String name        ArrayList<statemachine_Command> statemachine_commands,        ArrayList<statemachine_Transition> statemachine_transitions    ) {
        this.name = name;
        this.statemachine_commands = statemachine_commands;
        this.statemachine_transitions = statemachine_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public List<statemachine_Command> getStatemachine_commands() {
        return statemachine_commands;
    }

    public void addStatemachine_command(Statemachine_command statemachine_command) {
        this.statemachine_commands.add(statemachine_command);
    }
    public statemachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(statemachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public List<statemachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }

}