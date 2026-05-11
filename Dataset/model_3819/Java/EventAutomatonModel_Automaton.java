





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_Automaton  {

    private String name;





    private List<EventAutomatonModel_SymbolicParameter> eventautomatonmodel_symbolicparameters;




    private List<EventAutomatonModel_Token> eventautomatonmodel_tokens;




    private List<EventAutomatonModel_SymbolicTimer> eventautomatonmodel_symbolictimers;




    private EventAutomatonModel_ComplexEventProcessor eventautomatonmodel_complexeventprocessor;


    public EventAutomatonModel_Automaton(
        String name    ) {
        this.name = name;
        this.eventautomatonmodel_symbolicparameters = new ArrayList<>();
        this.eventautomatonmodel_tokens = new ArrayList<>();
        this.eventautomatonmodel_symbolictimers = new ArrayList<>();
    }

    public EventAutomatonModel_Automaton(
        String name        ArrayList<EventAutomatonModel_SymbolicParameter> eventautomatonmodel_symbolicparameters,        ArrayList<EventAutomatonModel_Token> eventautomatonmodel_tokens,        ArrayList<EventAutomatonModel_SymbolicTimer> eventautomatonmodel_symbolictimers    ) {
        this.name = name;
        this.eventautomatonmodel_symbolicparameters = eventautomatonmodel_symbolicparameters;
        this.eventautomatonmodel_tokens = eventautomatonmodel_tokens;
        this.eventautomatonmodel_symbolictimers = eventautomatonmodel_symbolictimers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<EventAutomatonModel_SymbolicParameter> getEventautomatonmodel_symbolicparameters() {
        return eventautomatonmodel_symbolicparameters;
    }

    public void addEventautomatonmodel_symbolicparameter(Eventautomatonmodel_symbolicparameter eventautomatonmodel_symbolicparameter) {
        this.eventautomatonmodel_symbolicparameters.add(eventautomatonmodel_symbolicparameter);
    }
    public List<EventAutomatonModel_Token> getEventautomatonmodel_tokens() {
        return eventautomatonmodel_tokens;
    }

    public void addEventautomatonmodel_token(Eventautomatonmodel_token eventautomatonmodel_token) {
        this.eventautomatonmodel_tokens.add(eventautomatonmodel_token);
    }
    public List<EventAutomatonModel_SymbolicTimer> getEventautomatonmodel_symbolictimers() {
        return eventautomatonmodel_symbolictimers;
    }

    public void addEventautomatonmodel_symbolictimer(Eventautomatonmodel_symbolictimer eventautomatonmodel_symbolictimer) {
        this.eventautomatonmodel_symbolictimers.add(eventautomatonmodel_symbolictimer);
    }
    public EventAutomatonModel_ComplexEventProcessor getEventautomatonmodel_complexeventprocessor() {
        return eventautomatonmodel_complexeventprocessor;
    }

    public void setEventautomatonmodel_complexeventprocessor(EventAutomatonModel_ComplexEventProcessor eventautomatonmodel_complexeventprocessor) {
        this.eventautomatonmodel_complexeventprocessor = eventautomatonmodel_complexeventprocessor;
    }

}