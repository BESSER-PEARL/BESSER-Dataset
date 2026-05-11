





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_StructuredActivityNode  {






    private BPMNProfile_EventBasedGateway bpmnprofile_eventbasedgateway;




    private BPMNProfile_SubProcess bpmnprofile_subprocess;




    private BPMNProfile_LoopCharacteristics bpmnprofile_loopcharacteristics;


    public BPMNProfile_StructuredActivityNode(
    ) {
    }



    public BPMNProfile_EventBasedGateway getBpmnprofile_eventbasedgateway() {
        return bpmnprofile_eventbasedgateway;
    }

    public void setBpmnprofile_eventbasedgateway(BPMNProfile_EventBasedGateway bpmnprofile_eventbasedgateway) {
        this.bpmnprofile_eventbasedgateway = bpmnprofile_eventbasedgateway;
    }
    public BPMNProfile_SubProcess getBpmnprofile_subprocess() {
        return bpmnprofile_subprocess;
    }

    public void setBpmnprofile_subprocess(BPMNProfile_SubProcess bpmnprofile_subprocess) {
        this.bpmnprofile_subprocess = bpmnprofile_subprocess;
    }
    public BPMNProfile_LoopCharacteristics getBpmnprofile_loopcharacteristics() {
        return bpmnprofile_loopcharacteristics;
    }

    public void setBpmnprofile_loopcharacteristics(BPMNProfile_LoopCharacteristics bpmnprofile_loopcharacteristics) {
        this.bpmnprofile_loopcharacteristics = bpmnprofile_loopcharacteristics;
    }

}