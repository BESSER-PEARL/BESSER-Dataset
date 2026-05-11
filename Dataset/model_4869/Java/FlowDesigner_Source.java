





import java.util.List;
import java.util.ArrayList;

public class FlowDesigner_Source  {






    private List<FlowDesigner_Event> flowdesigner_events;


    public FlowDesigner_Source(
    ) {
        this.flowdesigner_events = new ArrayList<>();
    }

    public FlowDesigner_Source(
        ArrayList<FlowDesigner_Event> flowdesigner_events    ) {
        this.flowdesigner_events = flowdesigner_events;
    }


    public List<FlowDesigner_Event> getFlowdesigner_events() {
        return flowdesigner_events;
    }

    public void addFlowdesigner_event(Flowdesigner_event flowdesigner_event) {
        this.flowdesigner_events.add(flowdesigner_event);
    }

}