





import java.util.List;
import java.util.ArrayList;

public class robotG_robot_Obstacle extends flow_ExprBool, robot_CommandeRobot {

    private int distance;



    public robotG_robot_Obstacle(
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