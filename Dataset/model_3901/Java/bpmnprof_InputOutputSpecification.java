





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_InputOutputSpecification extends BaseElement {






    private List<bpmnprof_OutputSet> bpmnprof_outputsets;


    public bpmnprof_InputOutputSpecification(
    ) {
        super(
        );
        this.bpmnprof_outputsets = new ArrayList<>();
    }

    public bpmnprof_InputOutputSpecification(
        ArrayList<bpmnprof_OutputSet> bpmnprof_outputsets    ) {
        this.bpmnprof_outputsets = bpmnprof_outputsets;
    }


    public List<bpmnprof_OutputSet> getBpmnprof_outputsets() {
        return bpmnprof_outputsets;
    }

    public void addBpmnprof_outputset(Bpmnprof_outputset bpmnprof_outputset) {
        this.bpmnprof_outputsets.add(bpmnprof_outputset);
    }

}