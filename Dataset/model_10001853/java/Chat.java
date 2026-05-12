





import java.util.List;
import java.util.ArrayList;

public class Chat  {

    private String commands;
    private String username;



    public Chat(
        String commands,        String username    ) {
        this.commands = commands;
        this.username = username;
    }


    public String getCommands() {
        return commands;
    }

    public void setCommands(String commands) {
        this.commands = commands;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}