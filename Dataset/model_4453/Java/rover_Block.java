





import java.util.List;
import java.util.ArrayList;

public class rover_Block  {






    private List<rover_Transition> rover_transitions;




    private rover_Repeat rover_repeat;




    private rover_Program rover_program;




    private List<rover_Command> rover_commands;


    public rover_Block(
    ) {
        this.rover_transitions = new ArrayList<>();
        this.rover_commands = new ArrayList<>();
    }

    public rover_Block(
        ArrayList<rover_Transition> rover_transitions,        ArrayList<rover_Command> rover_commands    ) {
        this.rover_transitions = rover_transitions;
        this.rover_commands = rover_commands;
    }


    public List<rover_Transition> getRover_transitions() {
        return rover_transitions;
    }

    public void addRover_transition(Rover_transition rover_transition) {
        this.rover_transitions.add(rover_transition);
    }
    public rover_Repeat getRover_repeat() {
        return rover_repeat;
    }

    public void setRover_repeat(rover_Repeat rover_repeat) {
        this.rover_repeat = rover_repeat;
    }
    public rover_Program getRover_program() {
        return rover_program;
    }

    public void setRover_program(rover_Program rover_program) {
        this.rover_program = rover_program;
    }
    public List<rover_Command> getRover_commands() {
        return rover_commands;
    }

    public void addRover_command(Rover_command rover_command) {
        this.rover_commands.add(rover_command);
    }

}