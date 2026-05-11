





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_SequenceFlow extends FlowElement {

    private String isImmediate;





    private BPMNProfile_ExclusiveGateway bpmnprofile_exclusivegateway;




    private BPMNProfile_InclusiveGateway bpmnprofile_inclusivegateway;




    private BPMNProfile_ComplexGateway bpmnprofile_complexgateway;




    private BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity;


    public BPMNProfile_SequenceFlow(
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

    public BPMNProfile_ExclusiveGateway getBpmnprofile_exclusivegateway() {
        return bpmnprofile_exclusivegateway;
    }

    public void setBpmnprofile_exclusivegateway(BPMNProfile_ExclusiveGateway bpmnprofile_exclusivegateway) {
        this.bpmnprofile_exclusivegateway = bpmnprofile_exclusivegateway;
    }
    public BPMNProfile_InclusiveGateway getBpmnprofile_inclusivegateway() {
        return bpmnprofile_inclusivegateway;
    }

    public void setBpmnprofile_inclusivegateway(BPMNProfile_InclusiveGateway bpmnprofile_inclusivegateway) {
        this.bpmnprofile_inclusivegateway = bpmnprofile_inclusivegateway;
    }
    public BPMNProfile_ComplexGateway getBpmnprofile_complexgateway() {
        return bpmnprofile_complexgateway;
    }

    public void setBpmnprofile_complexgateway(BPMNProfile_ComplexGateway bpmnprofile_complexgateway) {
        this.bpmnprofile_complexgateway = bpmnprofile_complexgateway;
    }
    public BPMNProfile_BPMNActivity getBpmnprofile_bpmnactivity() {
        return bpmnprofile_bpmnactivity;
    }

    public void setBpmnprofile_bpmnactivity(BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity) {
        this.bpmnprofile_bpmnactivity = bpmnprofile_bpmnactivity;
    }

}