





import java.util.List;
import java.util.ArrayList;

public class rover_DistanceSensor extends Sensor {

    private float remainingDistance;



    public rover_DistanceSensor(
        float remainingDistance    ) {
        super(
        );
        this.remainingDistance = remainingDistance;
    }


    public float getRemainingdistance() {
        return remainingDistance;
    }

    public void setRemainingdistance(float remainingDistance) {
        this.remainingDistance = remainingDistance;
    }


}