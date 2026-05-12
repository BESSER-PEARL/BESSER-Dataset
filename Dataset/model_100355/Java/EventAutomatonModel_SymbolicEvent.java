





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_SymbolicEvent  {






    private List<EventAutomatonModel_SymbolicParameter> eventautomatonmodel_symbolicparameters;


    public EventAutomatonModel_SymbolicEvent(
    ) {
        this.eventautomatonmodel_symbolicparameters = new ArrayList<>();
    }

    public EventAutomatonModel_SymbolicEvent(
        ArrayList<EventAutomatonModel_SymbolicParameter> eventautomatonmodel_symbolicparameters    ) {
        this.eventautomatonmodel_symbolicparameters = eventautomatonmodel_symbolicparameters;
    }


    public List<EventAutomatonModel_SymbolicParameter> getEventautomatonmodel_symbolicparameters() {
        return eventautomatonmodel_symbolicparameters;
    }

    public void addEventautomatonmodel_symbolicparameter(Eventautomatonmodel_symbolicparameter eventautomatonmodel_symbolicparameter) {
        this.eventautomatonmodel_symbolicparameters.add(eventautomatonmodel_symbolicparameter);
    }

}