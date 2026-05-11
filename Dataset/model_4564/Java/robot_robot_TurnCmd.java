





import java.util.List;
import java.util.ArrayList;

public class robot_robot_TurnCmd extends Command {

    private String angle;
    private String power;



    public robot_robot_TurnCmd(
        String angle,        String power    ) {
        super(
        );
        this.angle = angle;
        this.power = power;
    }


    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getPower() {
        return power;
    }

    public void setPower(String power) {
        this.power = power;
    }


}