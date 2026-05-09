





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_MoveForwardAndTurningLeftAction extends Action {

    private int startTick;
    private int speed;
    private int diff;
    private int duration;



    public ardurobotml_MoveForwardAndTurningLeftAction(
        int startTick,        int speed,        int diff,        int duration    ) {
        super(
        );
        this.startTick = startTick;
        this.speed = speed;
        this.diff = diff;
        this.duration = duration;
    }


    public int getStarttick() {
        return startTick;
    }

    public void setStarttick(int startTick) {
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


}