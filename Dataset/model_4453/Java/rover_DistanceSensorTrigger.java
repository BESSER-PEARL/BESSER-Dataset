





import java.util.List;
import java.util.ArrayList;

public class rover_DistanceSensorTrigger extends TriggeredTransition {






    private rover_Distance rover_distance;




    private rover_Length rover_length;


    public rover_DistanceSensorTrigger(
    ) {
        super(
        );
    }



    public rover_Distance getRover_distance() {
        return rover_distance;
    }

    public void setRover_distance(rover_Distance rover_distance) {
        this.rover_distance = rover_distance;
    }
    public rover_Length getRover_length() {
        return rover_length;
    }

    public void setRover_length(rover_Length rover_length) {
        this.rover_length = rover_length;
    }

}