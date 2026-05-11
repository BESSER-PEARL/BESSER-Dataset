





import java.util.List;
import java.util.ArrayList;

public class micro_Step extends NamedElement {






    private List<micro_Command> micro_commands;




    private micro_Saga micro_saga;


    public micro_Step(
    ) {
        super(
        );
        this.micro_commands = new ArrayList<>();
    }

    public micro_Step(
        ArrayList<micro_Command> micro_commands    ) {
        this.micro_commands = micro_commands;
    }


    public List<micro_Command> getMicro_commands() {
        return micro_commands;
    }

    public void addMicro_command(Micro_command micro_command) {
        this.micro_commands.add(micro_command);
    }
    public micro_Saga getMicro_saga() {
        return micro_saga;
    }

    public void setMicro_saga(micro_Saga micro_saga) {
        this.micro_saga = micro_saga;
    }

}