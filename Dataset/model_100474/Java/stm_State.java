





import java.util.List;
import java.util.ArrayList;

public class stm_State  {

    private String name;





    private List<stm_Command> stm_commands;




    private List<stm_SelfEvent> stm_selfevents;




    private List<stm_Transition> stm_transitions;




    private stm_Command stm_command;




    private stm_State stm_state;




    private stm_Transition stm_transition;




    private stm_Command stm_command;




    private stm_Statemachine stm_statemachine;




    private List<stm_Command> stm_commands;


    public stm_State(
        String name    ) {
        this.name = name;
        this.stm_commands = new ArrayList<>();
        this.stm_selfevents = new ArrayList<>();
        this.stm_transitions = new ArrayList<>();
        this.stm_commands = new ArrayList<>();
    }

    public stm_State(
        String name        ArrayList<stm_Command> stm_commands,        ArrayList<stm_SelfEvent> stm_selfevents,        ArrayList<stm_Transition> stm_transitions,        ArrayList<stm_Command> stm_commands    ) {
        this.name = name;
        this.stm_commands = stm_commands;
        this.stm_selfevents = stm_selfevents;
        this.stm_transitions = stm_transitions;
        this.stm_commands = stm_commands;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<stm_Command> getStm_commands() {
        return stm_commands;
    }

    public void addStm_command(Stm_command stm_command) {
        this.stm_commands.add(stm_command);
    }
    public List<stm_SelfEvent> getStm_selfevents() {
        return stm_selfevents;
    }

    public void addStm_selfevent(Stm_selfevent stm_selfevent) {
        this.stm_selfevents.add(stm_selfevent);
    }
    public List<stm_Transition> getStm_transitions() {
        return stm_transitions;
    }

    public void addStm_transition(Stm_transition stm_transition) {
        this.stm_transitions.add(stm_transition);
    }
    public stm_Command getStm_command() {
        return stm_command;
    }

    public void setStm_command(stm_Command stm_command) {
        this.stm_command = stm_command;
    }
    public stm_State getStm_state() {
        return stm_state;
    }

    public void setStm_state(stm_State stm_state) {
        this.stm_state = stm_state;
    }
    public stm_Transition getStm_transition() {
        return stm_transition;
    }

    public void setStm_transition(stm_Transition stm_transition) {
        this.stm_transition = stm_transition;
    }
    public stm_Command getStm_command() {
        return stm_command;
    }

    public void setStm_command(stm_Command stm_command) {
        this.stm_command = stm_command;
    }
    public stm_Statemachine getStm_statemachine() {
        return stm_statemachine;
    }

    public void setStm_statemachine(stm_Statemachine stm_statemachine) {
        this.stm_statemachine = stm_statemachine;
    }
    public List<stm_Command> getStm_commands() {
        return stm_commands;
    }

    public void addStm_command(Stm_command stm_command) {
        this.stm_commands.add(stm_command);
    }

}