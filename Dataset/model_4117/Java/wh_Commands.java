





import java.util.List;
import java.util.ArrayList;

public class wh_Commands  {

    private String command;





    private wh_Definition wh_definition;




    private wh_Commands wh_commands;


    public wh_Commands(
        String command    ) {
        this.command = command;
    }


    public String getCommand() {
        return command;
    }

    public void setCommand(String command) {
        this.command = command;
    }

    public wh_Definition getWh_definition() {
        return wh_definition;
    }

    public void setWh_definition(wh_Definition wh_definition) {
        this.wh_definition = wh_definition;
    }
    public wh_Commands getWh_commands() {
        return wh_commands;
    }

    public void setWh_commands(wh_Commands wh_commands) {
        this.wh_commands = wh_commands;
    }

}