





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_EventGuard  {






    private EventAutomatonModel_SymbolicEvent eventautomatonmodel_symbolicevent;




    private EventAutomatonModel_Transition eventautomatonmodel_transition;




    private List<EventAutomatonModel_Binding> eventautomatonmodel_bindings;


    public EventAutomatonModel_EventGuard(
    ) {
        this.eventautomatonmodel_bindings = new ArrayList<>();
    }

    public EventAutomatonModel_EventGuard(
        ArrayList<EventAutomatonModel_Binding> eventautomatonmodel_bindings    ) {
        this.eventautomatonmodel_bindings = eventautomatonmodel_bindings;
    }


    public EventAutomatonModel_SymbolicEvent getEventautomatonmodel_symbolicevent() {
        return eventautomatonmodel_symbolicevent;
    }

    public void setEventautomatonmodel_symbolicevent(EventAutomatonModel_SymbolicEvent eventautomatonmodel_symbolicevent) {
        this.eventautomatonmodel_symbolicevent = eventautomatonmodel_symbolicevent;
    }
    public EventAutomatonModel_Transition getEventautomatonmodel_transition() {
        return eventautomatonmodel_transition;
    }

    public void setEventautomatonmodel_transition(EventAutomatonModel_Transition eventautomatonmodel_transition) {
        this.eventautomatonmodel_transition = eventautomatonmodel_transition;
    }
    public List<EventAutomatonModel_Binding> getEventautomatonmodel_bindings() {
        return eventautomatonmodel_bindings;
    }

    public void addEventautomatonmodel_binding(Eventautomatonmodel_binding eventautomatonmodel_binding) {
        this.eventautomatonmodel_bindings.add(eventautomatonmodel_binding);
    }

}