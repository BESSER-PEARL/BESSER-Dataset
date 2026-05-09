





import java.util.List;
import java.util.ArrayList;

public class uml_TimeConstraint extends IntervalConstraint {

    private String firstEvent;



    public uml_TimeConstraint(
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