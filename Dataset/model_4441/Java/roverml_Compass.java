





import java.util.List;
import java.util.ArrayList;

public class roverml_Compass extends Sensor {

    private int angle;



    public roverml_Compass(
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


}