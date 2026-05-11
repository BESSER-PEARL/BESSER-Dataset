





import java.util.List;
import java.util.ArrayList;

public class cfgraph_ControlFlowEdge  {

    private boolean backward;





    private cfgraph_StatementVertex cfgraph_statementvertex;




    private cfgraph_BranchingVertex cfgraph_branchingvertex;




    private cfgraph_StartVertex cfgraph_startvertex;


    public cfgraph_ControlFlowEdge(
        boolean backward    ) {
        this.backward = backward;
    }


    public boolean getBackward() {
        return backward;
    }

    public void setBackward(boolean backward) {
        this.backward = backward;
    }

    public cfgraph_StatementVertex getCfgraph_statementvertex() {
        return cfgraph_statementvertex;
    }

    public void setCfgraph_statementvertex(cfgraph_StatementVertex cfgraph_statementvertex) {
        this.cfgraph_statementvertex = cfgraph_statementvertex;
    }
    public cfgraph_BranchingVertex getCfgraph_branchingvertex() {
        return cfgraph_branchingvertex;
    }

    public void setCfgraph_branchingvertex(cfgraph_BranchingVertex cfgraph_branchingvertex) {
        this.cfgraph_branchingvertex = cfgraph_branchingvertex;
    }
    public cfgraph_StartVertex getCfgraph_startvertex() {
        return cfgraph_startvertex;
    }

    public void setCfgraph_startvertex(cfgraph_StartVertex cfgraph_startvertex) {
        this.cfgraph_startvertex = cfgraph_startvertex;
    }

}