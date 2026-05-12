





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_ComplexEventProcessor  {






    private List<EventAutomatonModel_SymbolicInputEvent> eventautomatonmodel_symbolicinputevents;




    private List<EventAutomatonModel_Automaton> eventautomatonmodel_automatons;


    public EventAutomatonModel_ComplexEventProcessor(
    ) {
        this.eventautomatonmodel_symbolicinputevents = new ArrayList<>();
        this.eventautomatonmodel_automatons = new ArrayList<>();
    }

    public EventAutomatonModel_ComplexEventProcessor(
        ArrayList<EventAutomatonModel_SymbolicInputEvent> eventautomatonmodel_symbolicinputevents,        ArrayList<EventAutomatonModel_Automaton> eventautomatonmodel_automatons    ) {
        this.eventautomatonmodel_symbolicinputevents = eventautomatonmodel_symbolicinputevents;
        this.eventautomatonmodel_automatons = eventautomatonmodel_automatons;
    }


    public List<EventAutomatonModel_SymbolicInputEvent> getEventautomatonmodel_symbolicinputevents() {
        return eventautomatonmodel_symbolicinputevents;
    }

    public void addEventautomatonmodel_symbolicinputevent(Eventautomatonmodel_symbolicinputevent eventautomatonmodel_symbolicinputevent) {
        this.eventautomatonmodel_symbolicinputevents.add(eventautomatonmodel_symbolicinputevent);
    }
    public List<EventAutomatonModel_Automaton> getEventautomatonmodel_automatons() {
        return eventautomatonmodel_automatons;
    }

    public void addEventautomatonmodel_automaton(Eventautomatonmodel_automaton eventautomatonmodel_automaton) {
        this.eventautomatonmodel_automatons.add(eventautomatonmodel_automaton);
    }

}