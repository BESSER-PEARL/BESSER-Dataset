





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_InputSet extends BaseElement {






    private bpmnprof_InputOutputSpecification bpmnprof_inputoutputspecification;




    private bpmnprof_InputOutputBinding bpmnprof_inputoutputbinding;


    public bpmnprof_InputSet(
    ) {
        super(
        );
    }



    public bpmnprof_InputOutputSpecification getBpmnprof_inputoutputspecification() {
        return bpmnprof_inputoutputspecification;
    }

    public void setBpmnprof_inputoutputspecification(bpmnprof_InputOutputSpecification bpmnprof_inputoutputspecification) {
        this.bpmnprof_inputoutputspecification = bpmnprof_inputoutputspecification;
    }
    public bpmnprof_InputOutputBinding getBpmnprof_inputoutputbinding() {
        return bpmnprof_inputoutputbinding;
    }

    public void setBpmnprof_inputoutputbinding(bpmnprof_InputOutputBinding bpmnprof_inputoutputbinding) {
        this.bpmnprof_inputoutputbinding = bpmnprof_inputoutputbinding;
    }

}