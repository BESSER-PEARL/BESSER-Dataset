





import java.util.List;
import java.util.ArrayList;

public class xDrone_Forward extends Command {

    private String distance;



    public xDrone_Forward(
        String distance    ) {
        super(
        );
        this.distance = distance;
    }


    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }


}