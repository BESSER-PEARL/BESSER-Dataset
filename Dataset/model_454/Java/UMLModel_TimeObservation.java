





import java.util.List;
import java.util.ArrayList;

public class UMLModel_TimeObservation extends Observation {

    private String event;
    private String firstEvent;



    public UMLModel_TimeObservation(
        String event,        String firstEvent    ) {
        super(
        );
        this.event = event;
        this.firstEvent = firstEvent;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getFirstevent() {
        return firstEvent;
    }

    public void setFirstevent(String firstEvent) {
        this.firstEvent = firstEvent;
    }


}