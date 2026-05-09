





import java.util.List;
import java.util.ArrayList;

public class statemachine_State  {

    private String name;





    private List<statemachine_Command> statemachine_commands;




    private statemachine_Statemachine statemachine_statemachine;


    public statemachine_State(
        String name    ) {
        this.name = name;
        this.statemachine_commands = new ArrayList<>();
    }

    public statemachine_State(
        String name        ArrayList<statemachine_Command> statemachine_commands    ) {
        this.name = name;
        this.statemachine_commands = statemachine_commands;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statemachine_Command> getStatemachine_commands() {
        return statemachine_commands;
    }

    public void addStatemachine_command(Statemachine_command statemachine_command) {
        this.statemachine_commands.add(statemachine_command);
    }
    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}