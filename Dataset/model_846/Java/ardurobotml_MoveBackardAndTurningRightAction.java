





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_MoveBackardAndTurningRightAction extends Action {

    private int speed;
    private int diff;
    private int startTick;
    private int duration;



    public ardurobotml_MoveBackardAndTurningRightAction(
        int speed,        int diff,        int startTick,        int duration    ) {
        super(
        );
        this.speed = speed;
        this.diff = diff;
        this.startTick = startTick;
        this.duration = duration;
    }


    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }
    public int getDiff() {
        return diff;
    }

    public void setDiff(int diff) {
        this.diff = diff;
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


}