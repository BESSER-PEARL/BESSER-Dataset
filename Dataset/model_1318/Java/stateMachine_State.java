





import java.util.List;
import java.util.ArrayList;

public class stateMachine_State  {

    private String name;





    private List<stateMachine_Command> statemachine_commands;




    private stateMachine_StateMachine statemachine_statemachine;




    private stateMachine_StateMachine statemachine_statemachine;




    private stateMachine_StateMachine statemachine_statemachine;


    public stateMachine_State(
        String name    ) {
        this.name = name;
        this.statemachine_commands = new ArrayList<>();
    }

    public stateMachine_State(
        String name        ArrayList<stateMachine_Command> statemachine_commands    ) {
        this.name = name;
        this.statemachine_commands = statemachine_commands;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<stateMachine_Command> getStatemachine_commands() {
        return statemachine_commands;
    }

    public void addStatemachine_command(Statemachine_command statemachine_command) {
        this.statemachine_commands.add(statemachine_command);
    }
    public stateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(stateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public stateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(stateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public stateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(stateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}