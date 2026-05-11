





import java.util.List;
import java.util.ArrayList;

public class robotG_robot_Turn extends CommandeRobot {

    private int angle;
    private int power;



    public robotG_robot_Turn(
        int angle,        int power    ) {
        super(
        );
        this.angle = angle;
        this.power = power;
    }


    public int getAngle() {
        return angle;
    }

    public void setAngle(int angle) {
        this.angle = angle;
    }
    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }


}