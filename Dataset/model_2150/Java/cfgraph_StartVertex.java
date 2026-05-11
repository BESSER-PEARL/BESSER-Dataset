





import java.util.List;
import java.util.ArrayList;

public class cfgraph_StartVertex extends ControlFlowVertex {






    private cfgraph_ControlFlowGraph cfgraph_controlflowgraph;


    public cfgraph_StartVertex(
    ) {
        super(
        );
    }



    public cfgraph_ControlFlowGraph getCfgraph_controlflowgraph() {
        return cfgraph_controlflowgraph;
    }

    public void setCfgraph_controlflowgraph(cfgraph_ControlFlowGraph cfgraph_controlflowgraph) {
        this.cfgraph_controlflowgraph = cfgraph_controlflowgraph;
    }

}