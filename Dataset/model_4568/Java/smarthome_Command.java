





import java.util.List;
import java.util.ArrayList;

public class smarthome_Command  {

    private String command;





    private smarthome_Item smarthome_item;




    private smarthome_CommandConnection smarthome_commandconnection;


    public smarthome_Command(
        String command    ) {
        this.command = command;
    }


    public String getCommand() {
        return command;
    }

    public void setCommand(String command) {
        this.command = command;
    }

    public smarthome_Item getSmarthome_item() {
        return smarthome_item;
    }

    public void setSmarthome_item(smarthome_Item smarthome_item) {
        this.smarthome_item = smarthome_item;
    }
    public smarthome_CommandConnection getSmarthome_commandconnection() {
        return smarthome_commandconnection;
    }

    public void setSmarthome_commandconnection(smarthome_CommandConnection smarthome_commandconnection) {
        this.smarthome_commandconnection = smarthome_commandconnection;
    }

}