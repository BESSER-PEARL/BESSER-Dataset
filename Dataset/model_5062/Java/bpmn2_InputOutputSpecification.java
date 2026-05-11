





import java.util.List;
import java.util.ArrayList;

public class bpmn2_InputOutputSpecification extends BaseElement {






    private bpmn2_CallableElement bpmn2_callableelement;




    private List<bpmn2_OutputSet> bpmn2_outputsets;




    private List<bpmn2_InputSet> bpmn2_inputsets;


    public bpmn2_InputOutputSpecification(
    ) {
        super(
        );
        this.bpmn2_outputsets = new ArrayList<>();
        this.bpmn2_inputsets = new ArrayList<>();
    }

    public bpmn2_InputOutputSpecification(
        ArrayList<bpmn2_OutputSet> bpmn2_outputsets,        ArrayList<bpmn2_InputSet> bpmn2_inputsets    ) {
        this.bpmn2_outputsets = bpmn2_outputsets;
        this.bpmn2_inputsets = bpmn2_inputsets;
    }


    public bpmn2_CallableElement getBpmn2_callableelement() {
        return bpmn2_callableelement;
    }

    public void setBpmn2_callableelement(bpmn2_CallableElement bpmn2_callableelement) {
        this.bpmn2_callableelement = bpmn2_callableelement;
    }
    public List<bpmn2_OutputSet> getBpmn2_outputsets() {
        return bpmn2_outputsets;
    }

    public void addBpmn2_outputset(Bpmn2_outputset bpmn2_outputset) {
        this.bpmn2_outputsets.add(bpmn2_outputset);
    }
    public List<bpmn2_InputSet> getBpmn2_inputsets() {
        return bpmn2_inputsets;
    }

    public void addBpmn2_inputset(Bpmn2_inputset bpmn2_inputset) {
        this.bpmn2_inputsets.add(bpmn2_inputset);
    }

}