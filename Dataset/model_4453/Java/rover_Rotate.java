





import java.util.List;
import java.util.ArrayList;

public class rover_Rotate extends Command {






    private rover_Repeat rover_repeat;




    private rover_Angle rover_angle;


    public rover_Rotate(
    ) {
        super(
        );
    }



    public rover_Repeat getRover_repeat() {
        return rover_repeat;
    }

    public void setRover_repeat(rover_Repeat rover_repeat) {
        this.rover_repeat = rover_repeat;
    }
    public rover_Angle getRover_angle() {
        return rover_angle;
    }

    public void setRover_angle(rover_Angle rover_angle) {
        this.rover_angle = rover_angle;
    }

}