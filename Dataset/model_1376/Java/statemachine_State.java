





import java.util.List;
import java.util.ArrayList;

public class statemachine_State extends NamedElement {






    private statemachine_Statemachine statemachine_statemachine;




    private List<statemachine_Command> statemachine_commands;


    public statemachine_State(
    ) {
        super(
        );
        this.statemachine_commands = new ArrayList<>();
    }

    public statemachine_State(
        ArrayList<statemachine_Command> statemachine_commands    ) {
        this.statemachine_commands = statemachine_commands;
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

}