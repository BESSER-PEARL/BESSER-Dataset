





import java.util.List;
import java.util.ArrayList;

public class cbpmn_SplitGateway extends FlowNode {






    private cbpmn_Branch cbpmn_branch;




    private List<cbpmn_Branch> cbpmn_branchs;


    public cbpmn_SplitGateway(
    ) {
        super(
        );
        this.cbpmn_branchs = new ArrayList<>();
    }

    public cbpmn_SplitGateway(
        ArrayList<cbpmn_Branch> cbpmn_branchs    ) {
        this.cbpmn_branchs = cbpmn_branchs;
    }


    public cbpmn_Branch getCbpmn_branch() {
        return cbpmn_branch;
    }

    public void setCbpmn_branch(cbpmn_Branch cbpmn_branch) {
        this.cbpmn_branch = cbpmn_branch;
    }
    public List<cbpmn_Branch> getCbpmn_branchs() {
        return cbpmn_branchs;
    }

    public void addCbpmn_branch(Cbpmn_branch cbpmn_branch) {
        this.cbpmn_branchs.add(cbpmn_branch);
    }

}