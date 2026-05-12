





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_MoveForwardAndTurningLeftAction extends Action {

    private int diff;
    private int speed;
    private int startTick;
    private int duration;



    public ardurobotml_MoveForwardAndTurningLeftAction(
        int diff,        int speed,        int startTick,        int duration    ) {
        super(
        );
        this.diff = diff;
        this.speed = speed;
        this.startTick = startTick;
        this.duration = duration;
    }


    public int getDiff() {
        return diff;
    }

    public void setDiff(int diff) {
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


}