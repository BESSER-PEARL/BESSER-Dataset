





import java.util.List;
import java.util.ArrayList;

public class rover_System  {






    private List<rover_Rover> rover_rovers;




    private List<rover_Program> rover_programs;


    public rover_System(
    ) {
        this.rover_rovers = new ArrayList<>();
        this.rover_programs = new ArrayList<>();
    }

    public rover_System(
        ArrayList<rover_Rover> rover_rovers,        ArrayList<rover_Program> rover_programs    ) {
        this.rover_rovers = rover_rovers;
        this.rover_programs = rover_programs;
    }


    public List<rover_Rover> getRover_rovers() {
        return rover_rovers;
    }

    public void addRover_rover(Rover_rover rover_rover) {
        this.rover_rovers.add(rover_rover);
    }
    public List<rover_Program> getRover_programs() {
        return rover_programs;
    }

    public void addRover_program(Rover_program rover_program) {
        this.rover_programs.add(rover_program);
    }

}