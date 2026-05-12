





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_MoveForwardAction extends Action {

    private int startTick;
    private int speed;
    private int duration;



    public ardurobotml_MoveForwardAction(
        int startTick,        int speed,        int duration    ) {
        super(
        );
        this.startTick = startTick;
        this.speed = speed;
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
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }


}