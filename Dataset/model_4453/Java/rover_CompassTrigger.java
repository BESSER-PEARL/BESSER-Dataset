





import java.util.List;
import java.util.ArrayList;

public class rover_CompassTrigger extends TriggeredTransition {






    private rover_Compass rover_compass;




    private rover_Angle rover_angle;


    public rover_CompassTrigger(
    ) {
        super(
        );
    }



    public rover_Compass getRover_compass() {
        return rover_compass;
    }

    public void setRover_compass(rover_Compass rover_compass) {
        this.rover_compass = rover_compass;
    }
    public rover_Angle getRover_angle() {
        return rover_angle;
    }

    public void setRover_angle(rover_Angle rover_angle) {
        this.rover_angle = rover_angle;
    }

}