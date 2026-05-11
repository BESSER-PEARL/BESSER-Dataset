





import java.util.List;
import java.util.ArrayList;

public class roverml_Repeat extends Command {

    private int numberOfReps;





    private List<roverml_Command> roverml_commands;


    public roverml_Repeat(
        int numberOfReps    ) {
        super(
        );
        this.numberOfReps = numberOfReps;
        this.roverml_commands = new ArrayList<>();
    }

    public roverml_Repeat(
        int numberOfReps        ArrayList<roverml_Command> roverml_commands    ) {
        this.numberOfReps = numberOfReps;
        this.roverml_commands = roverml_commands;
    }

    public int getNumberofreps() {
        return numberOfReps;
    }

    public void setNumberofreps(int numberOfReps) {
        this.numberOfReps = numberOfReps;
    }

    public List<roverml_Command> getRoverml_commands() {
        return roverml_commands;
    }

    public void addRoverml_command(Roverml_command roverml_command) {
        this.roverml_commands.add(roverml_command);
    }

}