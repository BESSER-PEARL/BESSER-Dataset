





import java.util.List;
import java.util.ArrayList;

public class roverml_CompassTrigger extends Triggered {

    private int angle;





    private roverml_Angle roverml_angle;




    private roverml_Compass roverml_compass;


    public roverml_CompassTrigger(
        int angle    ) {
        super(
        );
        this.angle = angle;
    }


    public int getAngle() {
        return angle;
    }

    public void setAngle(int angle) {
        this.angle = angle;
    }

    public roverml_Angle getRoverml_angle() {
        return roverml_angle;
    }

    public void setRoverml_angle(roverml_Angle roverml_angle) {
        this.roverml_angle = roverml_angle;
    }
    public roverml_Compass getRoverml_compass() {
        return roverml_compass;
    }

    public void setRoverml_compass(roverml_Compass roverml_compass) {
        this.roverml_compass = roverml_compass;
    }

}