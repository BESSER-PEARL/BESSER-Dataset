





import java.util.List;
import java.util.ArrayList;

public class carnot_IEventHandlerOwner  {






    private List<carnot_EventHandlerType> carnot_eventhandlertypes;


    public carnot_IEventHandlerOwner(
    ) {
        this.carnot_eventhandlertypes = new ArrayList<>();
    }

    public carnot_IEventHandlerOwner(
        ArrayList<carnot_EventHandlerType> carnot_eventhandlertypes    ) {
        this.carnot_eventhandlertypes = carnot_eventhandlertypes;
    }


    public List<carnot_EventHandlerType> getCarnot_eventhandlertypes() {
        return carnot_eventhandlertypes;
    }

    public void addCarnot_eventhandlertype(Carnot_eventhandlertype carnot_eventhandlertype) {
        this.carnot_eventhandlertypes.add(carnot_eventhandlertype);
    }

}