





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_NotEquivalentRelation  {






    private List<EventAutomatonModel_State> eventautomatonmodel_states;


    public EventAutomatonModel_NotEquivalentRelation(
    ) {
        this.eventautomatonmodel_states = new ArrayList<>();
    }

    public EventAutomatonModel_NotEquivalentRelation(
        ArrayList<EventAutomatonModel_State> eventautomatonmodel_states    ) {
        this.eventautomatonmodel_states = eventautomatonmodel_states;
    }


    public List<EventAutomatonModel_State> getEventautomatonmodel_states() {
        return eventautomatonmodel_states;
    }

    public void addEventautomatonmodel_state(Eventautomatonmodel_state eventautomatonmodel_state) {
        this.eventautomatonmodel_states.add(eventautomatonmodel_state);
    }

}