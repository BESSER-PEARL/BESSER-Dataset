





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_InputOutputBinding extends BaseElement {






    private BPMNProfile_BPMNOperation bpmnprofile_bpmnoperation;




    private BPMNProfile_OutputSet bpmnprofile_outputset;


    public BPMNProfile_InputOutputBinding(
    ) {
        super(
        );
    }



    public BPMNProfile_BPMNOperation getBpmnprofile_bpmnoperation() {
        return bpmnprofile_bpmnoperation;
    }

    public void setBpmnprofile_bpmnoperation(BPMNProfile_BPMNOperation bpmnprofile_bpmnoperation) {
        this.bpmnprofile_bpmnoperation = bpmnprofile_bpmnoperation;
    }
    public BPMNProfile_OutputSet getBpmnprofile_outputset() {
        return bpmnprofile_outputset;
    }

    public void setBpmnprofile_outputset(BPMNProfile_OutputSet bpmnprofile_outputset) {
        this.bpmnprofile_outputset = bpmnprofile_outputset;
    }

}