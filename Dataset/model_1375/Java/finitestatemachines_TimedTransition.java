





import java.util.List;
import java.util.ArrayList;

public class finitestatemachines_TimedTransition extends Transition2 {

    private int duration;



    public finitestatemachines_TimedTransition(
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