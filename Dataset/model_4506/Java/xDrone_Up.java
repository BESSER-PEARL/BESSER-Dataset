





import java.util.List;
import java.util.ArrayList;

public class xDrone_Up extends Command {

    private String distance;



    public xDrone_Up(
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