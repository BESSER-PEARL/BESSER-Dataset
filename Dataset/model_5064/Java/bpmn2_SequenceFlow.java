





import java.util.List;
import java.util.ArrayList;

public class bpmn2_SequenceFlow extends FlowElement {

    private boolean isImmediate;





    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_ComplexGateway bpmn2_complexgateway;




    private bpmn2_ExclusiveGateway bpmn2_exclusivegateway;




    private bpmn2_FlowNode bpmn2_flownode;




    private bpmn2_FlowNode bpmn2_flownode;




    private bpmn2_FlowNode bpmn2_flownode;




    private bpmn2_InclusiveGateway bpmn2_inclusivegateway;




    private bpmn2_FlowNode bpmn2_flownode;




    private bpmn2_Expression bpmn2_expression;




    private bpmn2_Activity bpmn2_activity;


    public bpmn2_SequenceFlow(
        boolean isImmediate    ) {
        super(
        );
        this.isImmediate = isImmediate;
    }


    public boolean getIsimmediate() {
        return isImmediate;
    }

    public void setIsimmediate(boolean isImmediate) {
        this.isImmediate = isImmediate;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_ComplexGateway getBpmn2_complexgateway() {
        return bpmn2_complexgateway;
    }

    public void setBpmn2_complexgateway(bpmn2_ComplexGateway bpmn2_complexgateway) {
        this.bpmn2_complexgateway = bpmn2_complexgateway;
    }
    public bpmn2_ExclusiveGateway getBpmn2_exclusivegateway() {
        return bpmn2_exclusivegateway;
    }

    public void setBpmn2_exclusivegateway(bpmn2_ExclusiveGateway bpmn2_exclusivegateway) {
        this.bpmn2_exclusivegateway = bpmn2_exclusivegateway;
    }
    public bpmn2_FlowNode getBpmn2_flownode() {
        return bpmn2_flownode;
    }

    public void setBpmn2_flownode(bpmn2_FlowNode bpmn2_flownode) {
        this.bpmn2_flownode = bpmn2_flownode;
    }
    public bpmn2_FlowNode getBpmn2_flownode() {
        return bpmn2_flownode;
    }

    public void setBpmn2_flownode(bpmn2_FlowNode bpmn2_flownode) {
        this.bpmn2_flownode = bpmn2_flownode;
    }
    public bpmn2_FlowNode getBpmn2_flownode() {
        return bpmn2_flownode;
    }

    public void setBpmn2_flownode(bpmn2_FlowNode bpmn2_flownode) {
        this.bpmn2_flownode = bpmn2_flownode;
    }
    public bpmn2_InclusiveGateway getBpmn2_inclusivegateway() {
        return bpmn2_inclusivegateway;
    }

    public void setBpmn2_inclusivegateway(bpmn2_InclusiveGateway bpmn2_inclusivegateway) {
        this.bpmn2_inclusivegateway = bpmn2_inclusivegateway;
    }
    public bpmn2_FlowNode getBpmn2_flownode() {
        return bpmn2_flownode;
    }

    public void setBpmn2_flownode(bpmn2_FlowNode bpmn2_flownode) {
        this.bpmn2_flownode = bpmn2_flownode;
    }
    public bpmn2_Expression getBpmn2_expression() {
        return bpmn2_expression;
    }

    public void setBpmn2_expression(bpmn2_Expression bpmn2_expression) {
        this.bpmn2_expression = bpmn2_expression;
    }
    public bpmn2_Activity getBpmn2_activity() {
        return bpmn2_activity;
    }

    public void setBpmn2_activity(bpmn2_Activity bpmn2_activity) {
        this.bpmn2_activity = bpmn2_activity;
    }

}