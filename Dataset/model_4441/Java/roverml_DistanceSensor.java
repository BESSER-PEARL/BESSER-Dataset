





import java.util.List;
import java.util.ArrayList;

public class roverml_DistanceSensor extends Sensor {

    private float distance;



    public roverml_DistanceSensor(
        float distance    ) {
        super(
        );
        this.distance = distance;
    }


    public float getDistance() {
        return distance;
    }

    public void setDistance(float distance) {
        this.distance = distance;
    }


}