





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_DurationConstraint extends IntervalConstraint {

    private boolean firstEvent;





    private CompleteDSLPckg_DurationInterval completedslpckg_durationinterval;


    public CompleteDSLPckg_DurationConstraint(
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

    public CompleteDSLPckg_DurationInterval getCompletedslpckg_durationinterval() {
        return completedslpckg_durationinterval;
    }

    public void setCompletedslpckg_durationinterval(CompleteDSLPckg_DurationInterval completedslpckg_durationinterval) {
        this.completedslpckg_durationinterval = completedslpckg_durationinterval;
    }

}