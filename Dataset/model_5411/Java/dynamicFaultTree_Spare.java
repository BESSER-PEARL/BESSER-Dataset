





import java.util.List;
import java.util.ArrayList;

public class dynamicFaultTree_Spare extends Gate {






    private List<dynamicFaultTree_Event> dynamicfaulttree_events;


    public dynamicFaultTree_Spare(
    ) {
        super(
        );
        this.dynamicfaulttree_events = new ArrayList<>();
    }

    public dynamicFaultTree_Spare(
        ArrayList<dynamicFaultTree_Event> dynamicfaulttree_events    ) {
        this.dynamicfaulttree_events = dynamicfaulttree_events;
    }


    public List<dynamicFaultTree_Event> getDynamicfaulttree_events() {
        return dynamicfaulttree_events;
    }

    public void addDynamicfaulttree_event(Dynamicfaulttree_event dynamicfaulttree_event) {
        this.dynamicfaulttree_events.add(dynamicfaulttree_event);
    }

}