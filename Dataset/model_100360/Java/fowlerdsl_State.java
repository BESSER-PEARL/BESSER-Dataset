





import java.util.List;
import java.util.ArrayList;

public class fowlerdsl_State  {

    private String name;





    private List<fowlerdsl_Command> fowlerdsl_commands;




    private fowlerdsl_Statemachine fowlerdsl_statemachine;


    public fowlerdsl_State(
        String name    ) {
        this.name = name;
        this.fowlerdsl_commands = new ArrayList<>();
    }

    public fowlerdsl_State(
        String name        ArrayList<fowlerdsl_Command> fowlerdsl_commands    ) {
        this.name = name;
        this.fowlerdsl_commands = fowlerdsl_commands;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fowlerdsl_Command> getFowlerdsl_commands() {
        return fowlerdsl_commands;
    }

    public void addFowlerdsl_command(Fowlerdsl_command fowlerdsl_command) {
        this.fowlerdsl_commands.add(fowlerdsl_command);
    }
    public fowlerdsl_Statemachine getFowlerdsl_statemachine() {
        return fowlerdsl_statemachine;
    }

    public void setFowlerdsl_statemachine(fowlerdsl_Statemachine fowlerdsl_statemachine) {
        this.fowlerdsl_statemachine = fowlerdsl_statemachine;
    }

}