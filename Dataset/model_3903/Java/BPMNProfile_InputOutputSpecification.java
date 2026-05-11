





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_InputOutputSpecification extends BaseElement {






    private List<BPMNProfile_OutputSet> bpmnprofile_outputsets;




    private BPMNProfile_Task bpmnprofile_task;


    public BPMNProfile_InputOutputSpecification(
    ) {
        super(
        );
        this.bpmnprofile_outputsets = new ArrayList<>();
    }

    public BPMNProfile_InputOutputSpecification(
        ArrayList<BPMNProfile_OutputSet> bpmnprofile_outputsets    ) {
        this.bpmnprofile_outputsets = bpmnprofile_outputsets;
    }


    public List<BPMNProfile_OutputSet> getBpmnprofile_outputsets() {
        return bpmnprofile_outputsets;
    }

    public void addBpmnprofile_outputset(Bpmnprofile_outputset bpmnprofile_outputset) {
        this.bpmnprofile_outputsets.add(bpmnprofile_outputset);
    }
    public BPMNProfile_Task getBpmnprofile_task() {
        return bpmnprofile_task;
    }

    public void setBpmnprofile_task(BPMNProfile_Task bpmnprofile_task) {
        this.bpmnprofile_task = bpmnprofile_task;
    }

}