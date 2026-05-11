





import java.util.List;
import java.util.ArrayList;

public class cbpmn_FlowNode  {

    private String name;





    private cbpmn_Branch cbpmn_branch;




    private cbpmn_FlowNode cbpmn_flownode;




    private List<cbpmn_DataObjectReference> cbpmn_dataobjectreferences;




    private cbpmn_Branch cbpmn_branch;




    private cbpmn_FlowNode cbpmn_flownode;


    public cbpmn_FlowNode(
        String name    ) {
        this.name = name;
        this.cbpmn_dataobjectreferences = new ArrayList<>();
    }

    public cbpmn_FlowNode(
        String name        ArrayList<cbpmn_DataObjectReference> cbpmn_dataobjectreferences    ) {
        this.name = name;
        this.cbpmn_dataobjectreferences = cbpmn_dataobjectreferences;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cbpmn_Branch getCbpmn_branch() {
        return cbpmn_branch;
    }

    public void setCbpmn_branch(cbpmn_Branch cbpmn_branch) {
        this.cbpmn_branch = cbpmn_branch;
    }
    public cbpmn_FlowNode getCbpmn_flownode() {
        return cbpmn_flownode;
    }

    public void setCbpmn_flownode(cbpmn_FlowNode cbpmn_flownode) {
        this.cbpmn_flownode = cbpmn_flownode;
    }
    public List<cbpmn_DataObjectReference> getCbpmn_dataobjectreferences() {
        return cbpmn_dataobjectreferences;
    }

    public void addCbpmn_dataobjectreference(Cbpmn_dataobjectreference cbpmn_dataobjectreference) {
        this.cbpmn_dataobjectreferences.add(cbpmn_dataobjectreference);
    }
    public cbpmn_Branch getCbpmn_branch() {
        return cbpmn_branch;
    }

    public void setCbpmn_branch(cbpmn_Branch cbpmn_branch) {
        this.cbpmn_branch = cbpmn_branch;
    }
    public cbpmn_FlowNode getCbpmn_flownode() {
        return cbpmn_flownode;
    }

    public void setCbpmn_flownode(cbpmn_FlowNode cbpmn_flownode) {
        this.cbpmn_flownode = cbpmn_flownode;
    }

}