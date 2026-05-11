





import java.util.List;
import java.util.ArrayList;

public class robot_robot_HasTurnedCmd extends robot_Command, FlotCtrl_BoolExp {

    private String angle;



    public robot_robot_HasTurnedCmd(
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