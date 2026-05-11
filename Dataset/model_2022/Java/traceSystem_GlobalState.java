





import java.util.List;
import java.util.ArrayList;

public class traceSystem_GlobalState  {






    private traceSystem_Trace tracesystem_trace;




    private List<ForkedToken_baseToken_State> forkedtoken_basetoken_states;




    private List<EventOccurrence> eventoccurrences;


    public traceSystem_GlobalState(
    ) {
        this.forkedtoken_basetoken_states = new ArrayList<>();
        this.eventoccurrences = new ArrayList<>();
    }

    public traceSystem_GlobalState(
        ArrayList<ForkedToken_baseToken_State> forkedtoken_basetoken_states,        ArrayList<EventOccurrence> eventoccurrences    ) {
        this.forkedtoken_basetoken_states = forkedtoken_basetoken_states;
        this.eventoccurrences = eventoccurrences;
    }


    public traceSystem_Trace getTracesystem_trace() {
        return tracesystem_trace;
    }

    public void setTracesystem_trace(traceSystem_Trace tracesystem_trace) {
        this.tracesystem_trace = tracesystem_trace;
    }
    public List<ForkedToken_baseToken_State> getForkedtoken_basetoken_states() {
        return forkedtoken_basetoken_states;
    }

    public void addForkedtoken_basetoken_state(Forkedtoken_basetoken_state forkedtoken_basetoken_state) {
        this.forkedtoken_basetoken_states.add(forkedtoken_basetoken_state);
    }
    public List<EventOccurrence> getEventoccurrences() {
        return eventoccurrences;
    }

    public void addEventoccurrence(Eventoccurrence eventoccurrence) {
        this.eventoccurrences.add(eventoccurrence);
    }

}