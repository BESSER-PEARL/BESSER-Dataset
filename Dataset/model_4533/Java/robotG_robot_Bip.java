





import java.util.List;
import java.util.ArrayList;

public class robotG_robot_Bip extends CommandeRobot {

    private int duration;
    private boolean repeat;
    private int power;



    public robotG_robot_Bip(
        int duration,        boolean repeat,        int power    ) {
        super(
        );
        this.duration = duration;
        this.repeat = repeat;
        this.power = power;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public boolean getRepeat() {
        return repeat;
    }

    public void setRepeat(boolean repeat) {
        this.repeat = repeat;
    }
    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }


}