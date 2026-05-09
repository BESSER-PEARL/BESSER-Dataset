





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Command  {

    private String commandName;
    private String commandNo;
    private int commandProgParameter;





    private MachineLibrary_Commands machinelibrary_commands;


    public MachineLibrary_Command(
        String commandName,        String commandNo,        int commandProgParameter    ) {
        this.commandName = commandName;
        this.commandNo = commandNo;
        this.commandProgParameter = commandProgParameter;
    }


    public String getCommandname() {
        return commandName;
    }

    public void setCommandname(String commandName) {
        this.commandName = commandName;
    }
    public String getCommandno() {
        return commandNo;
    }

    public void setCommandno(String commandNo) {
        this.commandNo = commandNo;
    }
    public int getCommandprogparameter() {
        return commandProgParameter;
    }

    public void setCommandprogparameter(int commandProgParameter) {
        this.commandProgParameter = commandProgParameter;
    }

    public MachineLibrary_Commands getMachinelibrary_commands() {
        return machinelibrary_commands;
    }

    public void setMachinelibrary_commands(MachineLibrary_Commands machinelibrary_commands) {
        this.machinelibrary_commands = machinelibrary_commands;
    }

}