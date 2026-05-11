





import java.util.List;
import java.util.ArrayList;

public class flowgraph_Method extends Block, FlowInstr {






    private List<flowgraph_Var> flowgraph_vars;




    private flowgraph_Var flowgraph_var;


    public flowgraph_Method(
    ) {
        super(
        );
        this.flowgraph_vars = new ArrayList<>();
    }

    public flowgraph_Method(
        ArrayList<flowgraph_Var> flowgraph_vars    ) {
        this.flowgraph_vars = flowgraph_vars;
    }


    public List<flowgraph_Var> getFlowgraph_vars() {
        return flowgraph_vars;
    }

    public void addFlowgraph_var(Flowgraph_var flowgraph_var) {
        this.flowgraph_vars.add(flowgraph_var);
    }
    public flowgraph_Var getFlowgraph_var() {
        return flowgraph_var;
    }

    public void setFlowgraph_var(flowgraph_Var flowgraph_var) {
        this.flowgraph_var = flowgraph_var;
    }

}