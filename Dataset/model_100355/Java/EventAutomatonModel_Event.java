





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_Event  {






    private EventAutomatonModel_SymbolicEvent eventautomatonmodel_symbolicevent;




    private List<EventAutomatonModel_FixParameter> eventautomatonmodel_fixparameters;


    public EventAutomatonModel_Event(
    ) {
        this.eventautomatonmodel_fixparameters = new ArrayList<>();
    }

    public EventAutomatonModel_Event(
        ArrayList<EventAutomatonModel_FixParameter> eventautomatonmodel_fixparameters    ) {
        this.eventautomatonmodel_fixparameters = eventautomatonmodel_fixparameters;
    }


    public EventAutomatonModel_SymbolicEvent getEventautomatonmodel_symbolicevent() {
        return eventautomatonmodel_symbolicevent;
    }

    public void setEventautomatonmodel_symbolicevent(EventAutomatonModel_SymbolicEvent eventautomatonmodel_symbolicevent) {
        this.eventautomatonmodel_symbolicevent = eventautomatonmodel_symbolicevent;
    }
    public List<EventAutomatonModel_FixParameter> getEventautomatonmodel_fixparameters() {
        return eventautomatonmodel_fixparameters;
    }

    public void addEventautomatonmodel_fixparameter(Eventautomatonmodel_fixparameter eventautomatonmodel_fixparameter) {
        this.eventautomatonmodel_fixparameters.add(eventautomatonmodel_fixparameter);
    }

}