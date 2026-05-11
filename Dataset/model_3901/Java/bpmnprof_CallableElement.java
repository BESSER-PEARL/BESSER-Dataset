





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_CallableElement extends RootElement {






    private bpmnprof_InputOutputSpecification bpmnprof_inputoutputspecification;




    private List<bpmnprof_InputOutputBinding> bpmnprof_inputoutputbindings;


    public bpmnprof_CallableElement(
    ) {
        super(
        );
        this.bpmnprof_inputoutputbindings = new ArrayList<>();
    }

    public bpmnprof_CallableElement(
        ArrayList<bpmnprof_InputOutputBinding> bpmnprof_inputoutputbindings    ) {
        this.bpmnprof_inputoutputbindings = bpmnprof_inputoutputbindings;
    }


    public bpmnprof_InputOutputSpecification getBpmnprof_inputoutputspecification() {
        return bpmnprof_inputoutputspecification;
    }

    public void setBpmnprof_inputoutputspecification(bpmnprof_InputOutputSpecification bpmnprof_inputoutputspecification) {
        this.bpmnprof_inputoutputspecification = bpmnprof_inputoutputspecification;
    }
    public List<bpmnprof_InputOutputBinding> getBpmnprof_inputoutputbindings() {
        return bpmnprof_inputoutputbindings;
    }

    public void addBpmnprof_inputoutputbinding(Bpmnprof_inputoutputbinding bpmnprof_inputoutputbinding) {
        this.bpmnprof_inputoutputbindings.add(bpmnprof_inputoutputbinding);
    }

}