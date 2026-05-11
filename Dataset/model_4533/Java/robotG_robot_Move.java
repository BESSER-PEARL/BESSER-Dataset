





import java.util.List;
import java.util.ArrayList;

public class robotG_robot_Move extends CommandeRobot {

    private int power;



    public robotG_robot_Move(
        int power    ) {
        super(
        );
        this.power = power;
    }


    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }


}