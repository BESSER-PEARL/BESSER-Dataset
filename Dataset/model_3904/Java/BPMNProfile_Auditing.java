





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Auditing extends BaseElement {






    private BPMNProfile_FlowElement bpmnprofile_flowelement;




    private BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess;


    public BPMNProfile_Auditing(
    ) {
        super(
        );
    }



    public BPMNProfile_FlowElement getBpmnprofile_flowelement() {
        return bpmnprofile_flowelement;
    }

    public void setBpmnprofile_flowelement(BPMNProfile_FlowElement bpmnprofile_flowelement) {
        this.bpmnprofile_flowelement = bpmnprofile_flowelement;
    }
    public BPMNProfile_BPMNProcess getBpmnprofile_bpmnprocess() {
        return bpmnprofile_bpmnprocess;
    }

    public void setBpmnprofile_bpmnprocess(BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess) {
        this.bpmnprofile_bpmnprocess = bpmnprofile_bpmnprocess;
    }

}