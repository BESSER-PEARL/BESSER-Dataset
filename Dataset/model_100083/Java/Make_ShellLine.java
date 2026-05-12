





import java.util.List;
import java.util.ArrayList;

public class Make_ShellLine  {

    private String display;
    private String command;



    public Make_ShellLine(
        String display,        String command    ) {
        this.display = display;
        this.command = command;
    }


    public String getDisplay() {
        return display;
    }

    public void setDisplay(String display) {
        this.display = display;
    }
    public String getCommand() {
        return command;
    }

    public void setCommand(String command) {
        this.command = command;
    }


}