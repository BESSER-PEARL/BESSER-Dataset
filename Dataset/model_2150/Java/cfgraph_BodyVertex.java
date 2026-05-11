





import java.util.List;
import java.util.ArrayList;

public class cfgraph_BodyVertex extends ControlFlowVertex {






    private cfgraph_ControlFlowEdge cfgraph_controlflowedge;




    private List<cfgraph_ControlFlowEdge> cfgraph_controlflowedges;


    public cfgraph_BodyVertex(
    ) {
        super(
        );
        this.cfgraph_controlflowedges = new ArrayList<>();
    }

    public cfgraph_BodyVertex(
        ArrayList<cfgraph_ControlFlowEdge> cfgraph_controlflowedges    ) {
        this.cfgraph_controlflowedges = cfgraph_controlflowedges;
    }


    public cfgraph_ControlFlowEdge getCfgraph_controlflowedge() {
        return cfgraph_controlflowedge;
    }

    public void setCfgraph_controlflowedge(cfgraph_ControlFlowEdge cfgraph_controlflowedge) {
        this.cfgraph_controlflowedge = cfgraph_controlflowedge;
    }
    public List<cfgraph_ControlFlowEdge> getCfgraph_controlflowedges() {
        return cfgraph_controlflowedges;
    }

    public void addCfgraph_controlflowedge(Cfgraph_controlflowedge cfgraph_controlflowedge) {
        this.cfgraph_controlflowedges.add(cfgraph_controlflowedge);
    }

}