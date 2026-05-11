





import java.util.List;
import java.util.ArrayList;

public class cbpmn_FlowNodeInstance  {

    private String status;





    private cbpmn_ProcessInstance cbpmn_processinstance;




    private cbpmn_ProcessInstance cbpmn_processinstance;




    private cbpmn_FlowNode cbpmn_flownode;


    public cbpmn_FlowNodeInstance(
        String status    ) {
        this.status = status;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public cbpmn_ProcessInstance getCbpmn_processinstance() {
        return cbpmn_processinstance;
    }

    public void setCbpmn_processinstance(cbpmn_ProcessInstance cbpmn_processinstance) {
        this.cbpmn_processinstance = cbpmn_processinstance;
    }
    public cbpmn_ProcessInstance getCbpmn_processinstance() {
        return cbpmn_processinstance;
    }

    public void setCbpmn_processinstance(cbpmn_ProcessInstance cbpmn_processinstance) {
        this.cbpmn_processinstance = cbpmn_processinstance;
    }
    public cbpmn_FlowNode getCbpmn_flownode() {
        return cbpmn_flownode;
    }

    public void setCbpmn_flownode(cbpmn_FlowNode cbpmn_flownode) {
        this.cbpmn_flownode = cbpmn_flownode;
    }

}