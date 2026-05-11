





import java.util.List;
import java.util.ArrayList;

public class robot_robot_SetTurnAngleCmd extends Command {

    private String angle;



    public robot_robot_SetTurnAngleCmd(
        String angle    ) {
        super(
        );
        this.angle = angle;
    }


    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }


}