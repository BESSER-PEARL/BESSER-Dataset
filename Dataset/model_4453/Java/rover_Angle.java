





import java.util.List;
import java.util.ArrayList;

public class rover_Angle extends SingleQuantity {

    private String angleUnit;





    private rover_Compass rover_compass;


    public rover_Angle(
        String angleUnit    ) {
        super(
        );
        this.angleUnit = angleUnit;
    }


    public String getAngleunit() {
        return angleUnit;
    }

    public void setAngleunit(String angleUnit) {
        this.angleUnit = angleUnit;
    }

    public rover_Compass getRover_compass() {
        return rover_compass;
    }

    public void setRover_compass(rover_Compass rover_compass) {
        this.rover_compass = rover_compass;
    }

}