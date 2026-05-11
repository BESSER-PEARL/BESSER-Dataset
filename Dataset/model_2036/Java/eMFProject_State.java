





import java.util.List;
import java.util.ArrayList;

public class eMFProject_State  {

    private String name;





    private eMFProject_Statemachine emfproject_statemachine;




    private List<eMFProject_Command> emfproject_commands;




    private List<eMFProject_Transition> emfproject_transitions;




    private eMFProject_Transition emfproject_transition;


    public eMFProject_State(
        String name    ) {
        this.name = name;
        this.emfproject_commands = new ArrayList<>();
        this.emfproject_transitions = new ArrayList<>();
    }

    public eMFProject_State(
        String name        ArrayList<eMFProject_Command> emfproject_commands,        ArrayList<eMFProject_Transition> emfproject_transitions    ) {
        this.name = name;
        this.emfproject_commands = emfproject_commands;
        this.emfproject_transitions = emfproject_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eMFProject_Statemachine getEmfproject_statemachine() {
        return emfproject_statemachine;
    }

    public void setEmfproject_statemachine(eMFProject_Statemachine emfproject_statemachine) {
        this.emfproject_statemachine = emfproject_statemachine;
    }
    public List<eMFProject_Command> getEmfproject_commands() {
        return emfproject_commands;
    }

    public void addEmfproject_command(Emfproject_command emfproject_command) {
        this.emfproject_commands.add(emfproject_command);
    }
    public List<eMFProject_Transition> getEmfproject_transitions() {
        return emfproject_transitions;
    }

    public void addEmfproject_transition(Emfproject_transition emfproject_transition) {
        this.emfproject_transitions.add(emfproject_transition);
    }
    public eMFProject_Transition getEmfproject_transition() {
        return emfproject_transition;
    }

    public void setEmfproject_transition(eMFProject_Transition emfproject_transition) {
        this.emfproject_transition = emfproject_transition;
    }

}