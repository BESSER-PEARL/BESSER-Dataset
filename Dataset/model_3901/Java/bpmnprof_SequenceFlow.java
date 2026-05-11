





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_SequenceFlow extends FlowElement {

    private String isImmediate;





    private bpmnprof_ComplexGateway bpmnprof_complexgateway;




    private bpmnprof_InclusiveGateway bpmnprof_inclusivegateway;


    public bpmnprof_SequenceFlow(
        String isImmediate    ) {
        super(
        );
        this.isImmediate = isImmediate;
    }


    public String getIsimmediate() {
        return isImmediate;
    }

    public void setIsimmediate(String isImmediate) {
        this.isImmediate = isImmediate;
    }

    public bpmnprof_ComplexGateway getBpmnprof_complexgateway() {
        return bpmnprof_complexgateway;
    }

    public void setBpmnprof_complexgateway(bpmnprof_ComplexGateway bpmnprof_complexgateway) {
        this.bpmnprof_complexgateway = bpmnprof_complexgateway;
    }
    public bpmnprof_InclusiveGateway getBpmnprof_inclusivegateway() {
        return bpmnprof_inclusivegateway;
    }

    public void setBpmnprof_inclusivegateway(bpmnprof_InclusiveGateway bpmnprof_inclusivegateway) {
        this.bpmnprof_inclusivegateway = bpmnprof_inclusivegateway;
    }

}