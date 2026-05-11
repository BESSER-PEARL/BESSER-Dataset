





import java.util.List;
import java.util.ArrayList;

public class rover_GPS extends Sensor {

    private float currentPosition;



    public rover_GPS(
        float currentPosition    ) {
        super(
        );
        this.currentPosition = currentPosition;
    }


    public float getCurrentposition() {
        return currentPosition;
    }

    public void setCurrentposition(float currentPosition) {
        this.currentPosition = currentPosition;
    }


}