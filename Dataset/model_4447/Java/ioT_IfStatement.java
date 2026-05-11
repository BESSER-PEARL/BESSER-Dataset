





import java.util.List;
import java.util.ArrayList;

public class ioT_IfStatement extends Command {






    private List<ioT_Command> iot_commands;


    public ioT_IfStatement(
    ) {
        super(
        );
        this.iot_commands = new ArrayList<>();
    }

    public ioT_IfStatement(
        ArrayList<ioT_Command> iot_commands    ) {
        this.iot_commands = iot_commands;
    }


    public List<ioT_Command> getIot_commands() {
        return iot_commands;
    }

    public void addIot_command(Iot_command iot_command) {
        this.iot_commands.add(iot_command);
    }

}