





import java.util.List;
import java.util.ArrayList;

public class smDsl_CommandsSection  {






    private List<smDsl_Command> smdsl_commands;




    private smDsl_Model smdsl_model;


    public smDsl_CommandsSection(
    ) {
        this.smdsl_commands = new ArrayList<>();
    }

    public smDsl_CommandsSection(
        ArrayList<smDsl_Command> smdsl_commands    ) {
        this.smdsl_commands = smdsl_commands;
    }


    public List<smDsl_Command> getSmdsl_commands() {
        return smdsl_commands;
    }

    public void addSmdsl_command(Smdsl_command smdsl_command) {
        this.smdsl_commands.add(smdsl_command);
    }
    public smDsl_Model getSmdsl_model() {
        return smdsl_model;
    }

    public void setSmdsl_model(smDsl_Model smdsl_model) {
        this.smdsl_model = smdsl_model;
    }

}