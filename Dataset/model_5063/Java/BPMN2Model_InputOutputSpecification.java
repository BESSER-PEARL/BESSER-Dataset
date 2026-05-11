





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_InputOutputSpecification extends BaseElement {






    private BPMN2Model_Activity bpmn2model_activity;




    private List<BPMN2Model_OutputSet> bpmn2model_outputsets;




    private List<BPMN2Model_InputSet> bpmn2model_inputsets;


    public BPMN2Model_InputOutputSpecification(
    ) {
        super(
        );
        this.bpmn2model_outputsets = new ArrayList<>();
        this.bpmn2model_inputsets = new ArrayList<>();
    }

    public BPMN2Model_InputOutputSpecification(
        ArrayList<BPMN2Model_OutputSet> bpmn2model_outputsets,        ArrayList<BPMN2Model_InputSet> bpmn2model_inputsets    ) {
        this.bpmn2model_outputsets = bpmn2model_outputsets;
        this.bpmn2model_inputsets = bpmn2model_inputsets;
    }


    public BPMN2Model_Activity getBpmn2model_activity() {
        return bpmn2model_activity;
    }

    public void setBpmn2model_activity(BPMN2Model_Activity bpmn2model_activity) {
        this.bpmn2model_activity = bpmn2model_activity;
    }
    public List<BPMN2Model_OutputSet> getBpmn2model_outputsets() {
        return bpmn2model_outputsets;
    }

    public void addBpmn2model_outputset(Bpmn2model_outputset bpmn2model_outputset) {
        this.bpmn2model_outputsets.add(bpmn2model_outputset);
    }
    public List<BPMN2Model_InputSet> getBpmn2model_inputsets() {
        return bpmn2model_inputsets;
    }

    public void addBpmn2model_inputset(Bpmn2model_inputset bpmn2model_inputset) {
        this.bpmn2model_inputsets.add(bpmn2model_inputset);
    }

}