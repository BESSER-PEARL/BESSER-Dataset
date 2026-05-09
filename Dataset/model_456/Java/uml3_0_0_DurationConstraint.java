





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_DurationConstraint extends IntervalConstraint {

    private String firstEvent;



    public uml3_0_0_DurationConstraint(
        String firstEvent    ) {
        super(
        );
        this.firstEvent = firstEvent;
    }


    public String getFirstevent() {
        return firstEvent;
    }

    public void setFirstevent(String firstEvent) {
        this.firstEvent = firstEvent;
    }


}