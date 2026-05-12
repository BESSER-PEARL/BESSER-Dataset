





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_MoveBackardAction extends Action {

    private int duration;
    private int speed;
    private int startTick;



    public ardurobotml_MoveBackardAction(
        int duration,        int speed,        int startTick    ) {
        super(
        );
        this.duration = duration;
        this.speed = speed;
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
    public int getStarttick() {
        return startTick;
    }

    public void setStarttick(int startTick) {
        this.startTick = startTick;
    }


}