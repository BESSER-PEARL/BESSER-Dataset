





import java.util.List;
import java.util.ArrayList;

public class polybot_Move extends Instruction {

    private int duration;
    private int speed;



    public polybot_Move(
        int duration,        int speed    ) {
        super(
        );
        this.duration = duration;
        this.speed = speed;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }


}