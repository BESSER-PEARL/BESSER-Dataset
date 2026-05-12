





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_MoveBackardAndTurningLeftAction extends Action {

    private int speed;
    private int diff;
    private int duration;
    private int startTick;



    public ardurobotml_MoveBackardAndTurningLeftAction(
        int speed,        int diff,        int duration,        int startTick    ) {
        super(
        );
        this.speed = speed;
        this.diff = diff;
        this.duration = duration;
        this.startTick = startTick;
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
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public int getStarttick() {
        return startTick;
    }

    public void setStarttick(int startTick) {
        this.startTick = startTick;
    }


}