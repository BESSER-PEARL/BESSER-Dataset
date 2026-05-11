





import java.util.List;
import java.util.ArrayList;

public class flowgraph_FlowInstr extends Item {






    private List<flowgraph_FlowInstr> flowgraph_flowinstrs;




    private flowgraph_FlowInstr flowgraph_flowinstr;




    private flowgraph_Var flowgraph_var;




    private flowgraph_Var flowgraph_var;




    private List<flowgraph_FlowInstr> flowgraph_flowinstrs;




    private List<flowgraph_Var> flowgraph_vars;




    private List<flowgraph_Var> flowgraph_vars;


    public flowgraph_FlowInstr(
    ) {
        super(
        );
        this.flowgraph_flowinstrs = new ArrayList<>();
        this.flowgraph_flowinstrs = new ArrayList<>();
        this.flowgraph_vars = new ArrayList<>();
        this.flowgraph_vars = new ArrayList<>();
    }

    public flowgraph_FlowInstr(
        ArrayList<flowgraph_FlowInstr> flowgraph_flowinstrs,        ArrayList<flowgraph_FlowInstr> flowgraph_flowinstrs,        ArrayList<flowgraph_Var> flowgraph_vars,        ArrayList<flowgraph_Var> flowgraph_vars    ) {
        this.flowgraph_flowinstrs = flowgraph_flowinstrs;
        this.flowgraph_flowinstrs = flowgraph_flowinstrs;
        this.flowgraph_vars = flowgraph_vars;
        this.flowgraph_vars = flowgraph_vars;
    }


    public List<flowgraph_FlowInstr> getFlowgraph_flowinstrs() {
        return flowgraph_flowinstrs;
    }

    public void addFlowgraph_flowinstr(Flowgraph_flowinstr flowgraph_flowinstr) {
        this.flowgraph_flowinstrs.add(flowgraph_flowinstr);
    }
    public flowgraph_FlowInstr getFlowgraph_flowinstr() {
        return flowgraph_flowinstr;
    }

    public void setFlowgraph_flowinstr(flowgraph_FlowInstr flowgraph_flowinstr) {
        this.flowgraph_flowinstr = flowgraph_flowinstr;
    }
    public flowgraph_Var getFlowgraph_var() {
        return flowgraph_var;
    }

    public void setFlowgraph_var(flowgraph_Var flowgraph_var) {
        this.flowgraph_var = flowgraph_var;
    }
    public flowgraph_Var getFlowgraph_var() {
        return flowgraph_var;
    }

    public void setFlowgraph_var(flowgraph_Var flowgraph_var) {
        this.flowgraph_var = flowgraph_var;
    }
    public List<flowgraph_FlowInstr> getFlowgraph_flowinstrs() {
        return flowgraph_flowinstrs;
    }

    public void addFlowgraph_flowinstr(Flowgraph_flowinstr flowgraph_flowinstr) {
        this.flowgraph_flowinstrs.add(flowgraph_flowinstr);
    }
    public List<flowgraph_Var> getFlowgraph_vars() {
        return flowgraph_vars;
    }

    public void addFlowgraph_var(Flowgraph_var flowgraph_var) {
        this.flowgraph_vars.add(flowgraph_var);
    }
    public List<flowgraph_Var> getFlowgraph_vars() {
        return flowgraph_vars;
    }

    public void addFlowgraph_var(Flowgraph_var flowgraph_var) {
        this.flowgraph_vars.add(flowgraph_var);
    }

}