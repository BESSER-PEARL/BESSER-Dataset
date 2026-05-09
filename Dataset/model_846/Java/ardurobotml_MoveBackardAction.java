





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_MoveBackardAction extends Action {

    private int duration;
    private int startTick;
    private int speed;



    public ardurobotml_MoveBackardAction(
        int duration,        int startTick,        int speed    ) {
        super(
        );
        this.duration = duration;
        this.startTick = startTick;
        this.speed = speed;
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
    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }


}