





import java.util.List;
import java.util.ArrayList;

public class logo_Move extends Command {

    private float distance;



    public logo_Move(
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