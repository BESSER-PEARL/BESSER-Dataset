





import java.util.List;
import java.util.ArrayList;

public class robot_robot_ObstacleCmd extends robot_Command, FlotCtrl_BoolExp {

    private String distance;



    public robot_robot_ObstacleCmd(
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