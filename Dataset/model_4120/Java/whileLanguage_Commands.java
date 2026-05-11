





import java.util.List;
import java.util.ArrayList;

public class whileLanguage_Commands  {






    private whileLanguage_Definition whilelanguage_definition;




    private whileLanguage_Foreach whilelanguage_foreach;




    private List<whileLanguage_Command> whilelanguage_commands;


    public whileLanguage_Commands(
    ) {
        this.whilelanguage_commands = new ArrayList<>();
    }

    public whileLanguage_Commands(
        ArrayList<whileLanguage_Command> whilelanguage_commands    ) {
        this.whilelanguage_commands = whilelanguage_commands;
    }


    public whileLanguage_Definition getWhilelanguage_definition() {
        return whilelanguage_definition;
    }

    public void setWhilelanguage_definition(whileLanguage_Definition whilelanguage_definition) {
        this.whilelanguage_definition = whilelanguage_definition;
    }
    public whileLanguage_Foreach getWhilelanguage_foreach() {
        return whilelanguage_foreach;
    }

    public void setWhilelanguage_foreach(whileLanguage_Foreach whilelanguage_foreach) {
        this.whilelanguage_foreach = whilelanguage_foreach;
    }
    public List<whileLanguage_Command> getWhilelanguage_commands() {
        return whilelanguage_commands;
    }

    public void addWhilelanguage_command(Whilelanguage_command whilelanguage_command) {
        this.whilelanguage_commands.add(whilelanguage_command);
    }

}