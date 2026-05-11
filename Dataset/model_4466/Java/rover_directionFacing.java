





import java.util.List;
import java.util.ArrayList;

public class rover_directionFacing extends Sensor {

    private float currentlyFacing;



    public rover_directionFacing(
        float currentlyFacing    ) {
        super(
        );
        this.currentlyFacing = currentlyFacing;
    }


    public float getCurrentlyfacing() {
        return currentlyFacing;
    }

    public void setCurrentlyfacing(float currentlyFacing) {
        this.currentlyFacing = currentlyFacing;
    }


}