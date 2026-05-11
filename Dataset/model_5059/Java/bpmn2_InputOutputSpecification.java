





import java.util.List;
import java.util.ArrayList;

public class bpmn2_InputOutputSpecification extends BaseElement {






    private bpmn2_Activity bpmn2_activity;




    private List<bpmn2_OutputSet> bpmn2_outputsets;




    private bpmn2_CallableElement bpmn2_callableelement;


    public bpmn2_InputOutputSpecification(
    ) {
        super(
        );
        this.bpmn2_outputsets = new ArrayList<>();
    }

    public bpmn2_InputOutputSpecification(
        ArrayList<bpmn2_OutputSet> bpmn2_outputsets    ) {
        this.bpmn2_outputsets = bpmn2_outputsets;
    }


    public bpmn2_Activity getBpmn2_activity() {
        return bpmn2_activity;
    }

    public void setBpmn2_activity(bpmn2_Activity bpmn2_activity) {
        this.bpmn2_activity = bpmn2_activity;
    }
    public List<bpmn2_OutputSet> getBpmn2_outputsets() {
        return bpmn2_outputsets;
    }

    public void addBpmn2_outputset(Bpmn2_outputset bpmn2_outputset) {
        this.bpmn2_outputsets.add(bpmn2_outputset);
    }
    public bpmn2_CallableElement getBpmn2_callableelement() {
        return bpmn2_callableelement;
    }

    public void setBpmn2_callableelement(bpmn2_CallableElement bpmn2_callableelement) {
        this.bpmn2_callableelement = bpmn2_callableelement;
    }

}