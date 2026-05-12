





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_MoveBackardAndTurningRightAction extends Action {

    private int diff;
    private int startTick;
    private int duration;
    private int speed;



    public ardurobotml_MoveBackardAndTurningRightAction(
        int diff,        int startTick,        int duration,        int speed    ) {
        super(
        );
        this.diff = diff;
        this.startTick = startTick;
        this.duration = duration;
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
    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }


}