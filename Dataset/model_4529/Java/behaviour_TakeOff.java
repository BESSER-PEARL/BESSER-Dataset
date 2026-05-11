





import java.util.List;
import java.util.ArrayList;

public class behaviour_TakeOff extends Move {

    private float altitude;



    public behaviour_TakeOff(
        float altitude    ) {
        super(
        );
        this.altitude = altitude;
    }


    public float getAltitude() {
        return altitude;
    }

    public void setAltitude(float altitude) {
        this.altitude = altitude;
    }


}