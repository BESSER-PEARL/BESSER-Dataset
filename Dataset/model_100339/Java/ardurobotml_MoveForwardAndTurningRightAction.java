





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_MoveForwardAndTurningRightAction extends Action {

    private int speed;
    private int startTick;
    private int duration;
    private int diff;



    public ardurobotml_MoveForwardAndTurningRightAction(
        int speed,        int startTick,        int duration,        int diff    ) {
        super(
        );
        this.speed = speed;
        this.startTick = startTick;
        this.duration = duration;
        this.diff = diff;
    }


    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }
    public int getStarttick() {
        return startTick;
    }

    public void setStarttick(int startTick) {
        this.startTick = startTick;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public int getDiff() {
        return diff;
    }

    public void setDiff(int diff) {
        this.diff = diff;
    }


}