





import java.util.List;
import java.util.ArrayList;

public class robot_robot_MoveCmd extends Command {

    private String power;



    public robot_robot_MoveCmd(
        String power    ) {
        super(
        );
        this.power = power;
    }


    public String getPower() {
        return power;
    }

    public void setPower(String power) {
        this.power = power;
    }


}