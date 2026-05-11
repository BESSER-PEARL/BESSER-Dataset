





import java.util.List;
import java.util.ArrayList;

public class wh_Command  {

    private String cmd;





    private wh_Commands wh_commands;


    public wh_Command(
        String cmd    ) {
        this.cmd = cmd;
    }


    public String getCmd() {
        return cmd;
    }

    public void setCmd(String cmd) {
        this.cmd = cmd;
    }

    public wh_Commands getWh_commands() {
        return wh_commands;
    }

    public void setWh_commands(wh_Commands wh_commands) {
        this.wh_commands = wh_commands;
    }

}