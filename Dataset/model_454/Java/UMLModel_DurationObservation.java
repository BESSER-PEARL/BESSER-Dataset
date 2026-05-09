





import java.util.List;
import java.util.ArrayList;

public class UMLModel_DurationObservation extends Observation {

    private String firstEvent;
    private String event;



    public UMLModel_DurationObservation(
        String firstEvent,        String event    ) {
        super(
        );
        this.firstEvent = firstEvent;
        this.event = event;
    }


    public String getFirstevent() {
        return firstEvent;
    }

    public void setFirstevent(String firstEvent) {
        this.firstEvent = firstEvent;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }


}