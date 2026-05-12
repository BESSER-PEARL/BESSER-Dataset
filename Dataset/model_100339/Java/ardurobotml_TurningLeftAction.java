





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_TurningLeftAction extends Action {

    private int speed;
    private int startTick;
    private int duration;



    public ardurobotml_TurningLeftAction(
        int speed,        int startTick,        int duration    ) {
        super(
        );
        this.speed = speed;
        this.startTick = startTick;
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
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }


}