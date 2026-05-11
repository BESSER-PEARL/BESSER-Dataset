





import java.util.List;
import java.util.ArrayList;

public class ioT_ElseBlock  {






    private ioT_IfStatement iot_ifstatement;




    private List<ioT_Command> iot_commands;


    public ioT_ElseBlock(
    ) {
        this.iot_commands = new ArrayList<>();
    }

    public ioT_ElseBlock(
        ArrayList<ioT_Command> iot_commands    ) {
        this.iot_commands = iot_commands;
    }


    public ioT_IfStatement getIot_ifstatement() {
        return iot_ifstatement;
    }

    public void setIot_ifstatement(ioT_IfStatement iot_ifstatement) {
        this.iot_ifstatement = iot_ifstatement;
    }
    public List<ioT_Command> getIot_commands() {
        return iot_commands;
    }

    public void addIot_command(Iot_command iot_command) {
        this.iot_commands.add(iot_command);
    }

}