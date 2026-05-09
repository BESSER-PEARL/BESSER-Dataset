





import java.util.List;
import java.util.ArrayList;

public class fsm_TimedTransition extends Transition {

    private int duration;



    public fsm_TimedTransition(
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