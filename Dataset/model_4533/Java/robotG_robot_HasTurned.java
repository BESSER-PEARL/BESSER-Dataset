





import java.util.List;
import java.util.ArrayList;

public class robotG_robot_HasTurned extends flow_ExprBool, robot_CommandeRobot {

    private int angle;



    public robotG_robot_HasTurned(
        int angle    ) {
        super(
        );
        this.angle = angle;
    }


    public int getAngle() {
        return angle;
    }

    public void setAngle(int angle) {
        this.angle = angle;
    }


}