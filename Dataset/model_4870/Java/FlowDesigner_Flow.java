





import java.util.List;
import java.util.ArrayList;

public class FlowDesigner_Flow  {






    private FlowDesigner_InitialState flowdesigner_initialstate;




    private List<FlowDesigner_NamedState> flowdesigner_namedstates;




    private FlowDesigner_FinalState flowdesigner_finalstate;


    public FlowDesigner_Flow(
    ) {
        this.flowdesigner_namedstates = new ArrayList<>();
    }

    public FlowDesigner_Flow(
        ArrayList<FlowDesigner_NamedState> flowdesigner_namedstates    ) {
        this.flowdesigner_namedstates = flowdesigner_namedstates;
    }


    public FlowDesigner_InitialState getFlowdesigner_initialstate() {
        return flowdesigner_initialstate;
    }

    public void setFlowdesigner_initialstate(FlowDesigner_InitialState flowdesigner_initialstate) {
        this.flowdesigner_initialstate = flowdesigner_initialstate;
    }
    public List<FlowDesigner_NamedState> getFlowdesigner_namedstates() {
        return flowdesigner_namedstates;
    }

    public void addFlowdesigner_namedstate(Flowdesigner_namedstate flowdesigner_namedstate) {
        this.flowdesigner_namedstates.add(flowdesigner_namedstate);
    }
    public FlowDesigner_FinalState getFlowdesigner_finalstate() {
        return flowdesigner_finalstate;
    }

    public void setFlowdesigner_finalstate(FlowDesigner_FinalState flowdesigner_finalstate) {
        this.flowdesigner_finalstate = flowdesigner_finalstate;
    }

}