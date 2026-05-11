





import java.util.List;
import java.util.ArrayList;

public class CommonBehavior_SimpleTime_TimeConstraint extends IntervalConstraint {

    private boolean firstEvent;



    public CommonBehavior_SimpleTime_TimeConstraint(
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


}