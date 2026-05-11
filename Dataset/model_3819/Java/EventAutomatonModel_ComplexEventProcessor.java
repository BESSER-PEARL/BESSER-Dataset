





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_ComplexEventProcessor  {






    private List<EventAutomatonModel_SymbolicInputEvent> eventautomatonmodel_symbolicinputevents;


    public EventAutomatonModel_ComplexEventProcessor(
    ) {
        this.eventautomatonmodel_symbolicinputevents = new ArrayList<>();
    }

    public EventAutomatonModel_ComplexEventProcessor(
        ArrayList<EventAutomatonModel_SymbolicInputEvent> eventautomatonmodel_symbolicinputevents    ) {
        this.eventautomatonmodel_symbolicinputevents = eventautomatonmodel_symbolicinputevents;
    }


    public List<EventAutomatonModel_SymbolicInputEvent> getEventautomatonmodel_symbolicinputevents() {
        return eventautomatonmodel_symbolicinputevents;
    }

    public void addEventautomatonmodel_symbolicinputevent(Eventautomatonmodel_symbolicinputevent eventautomatonmodel_symbolicinputevent) {
        this.eventautomatonmodel_symbolicinputevents.add(eventautomatonmodel_symbolicinputevent);
    }

}