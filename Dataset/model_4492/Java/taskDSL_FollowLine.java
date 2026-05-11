





import java.util.List;
import java.util.ArrayList;

public class taskDSL_FollowLine extends Action {

    private int distance;



    public taskDSL_FollowLine(
        int distance    ) {
        super(
        );
        this.distance = distance;
    }


    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }


}