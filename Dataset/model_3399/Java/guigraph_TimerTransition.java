





import java.util.List;
import java.util.ArrayList;

public class guigraph_TimerTransition extends Transition {

    private int duration;



    public guigraph_TimerTransition(
        int duration    ) {
        super(
        );
        this.duration = duration;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }


}