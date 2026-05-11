





import java.util.List;
import java.util.ArrayList;

public class rover_GPS extends Sensor {






    private rover_GPSTrigger rover_gpstrigger;




    private rover_Position rover_position;


    public rover_GPS(
    ) {
        super(
        );
    }



    public rover_GPSTrigger getRover_gpstrigger() {
        return rover_gpstrigger;
    }

    public void setRover_gpstrigger(rover_GPSTrigger rover_gpstrigger) {
        this.rover_gpstrigger = rover_gpstrigger;
    }
    public rover_Position getRover_position() {
        return rover_position;
    }

    public void setRover_position(rover_Position rover_position) {
        this.rover_position = rover_position;
    }

}