





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_TimeConstraint extends IntervalConstraint {

    private boolean firstEvent;





    private CompleteDSLPckg_TimeInterval completedslpckg_timeinterval;


    public CompleteDSLPckg_TimeConstraint(
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

    public CompleteDSLPckg_TimeInterval getCompletedslpckg_timeinterval() {
        return completedslpckg_timeinterval;
    }

    public void setCompletedslpckg_timeinterval(CompleteDSLPckg_TimeInterval completedslpckg_timeinterval) {
        this.completedslpckg_timeinterval = completedslpckg_timeinterval;
    }

}