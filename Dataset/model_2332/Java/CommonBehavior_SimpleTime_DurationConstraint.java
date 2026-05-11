





import java.util.List;
import java.util.ArrayList;

public class CommonBehavior_SimpleTime_DurationConstraint extends IntervalConstraint {

    private boolean firstEvent;





    private DurationInterval durationinterval;


    public CommonBehavior_SimpleTime_DurationConstraint(
        boolean firstEvent    ) {
        super(
        );
        this.firstEvent = firstEvent;
    }


    public boolean getFirstevent() {
        return firstEvent;
    }

    public void setFirstevent(boolean firstEvent) {
        this.firstEvent = firstEvent;
    }

    public DurationInterval getDurationinterval() {
        return durationinterval;
    }

    public void setDurationinterval(DurationInterval durationinterval) {
        this.durationinterval = durationinterval;
    }

}