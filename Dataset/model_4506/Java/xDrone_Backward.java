





import java.util.List;
import java.util.ArrayList;

public class xDrone_Backward extends Command {

    private String distance;



    public xDrone_Backward(
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