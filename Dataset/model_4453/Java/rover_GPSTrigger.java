





import java.util.List;
import java.util.ArrayList;

public class rover_GPSTrigger extends TriggeredTransition {






    private rover_Position rover_position;


    public rover_GPSTrigger(
    ) {
        super(
        );
    }



    public rover_Position getRover_position() {
        return rover_position;
    }

    public void setRover_position(rover_Position rover_position) {
        this.rover_position = rover_position;
    }

}