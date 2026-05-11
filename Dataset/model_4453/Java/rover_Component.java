





import java.util.List;
import java.util.ArrayList;

public class rover_Component  {

    private String name;





    private rover_Rover rover_rover;


    public rover_Component(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rover_Rover getRover_rover() {
        return rover_rover;
    }

    public void setRover_rover(rover_Rover rover_rover) {
        this.rover_rover = rover_rover;
    }

}