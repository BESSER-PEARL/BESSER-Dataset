





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_CatchEvent extends Event {

    private boolean parallelMultiple;





    private List<BPMN2Model_EventDefinition> bpmn2model_eventdefinitions;




    private BPMN2Model_OutputSet bpmn2model_outputset;




    private List<BPMN2Model_EventDefinition> bpmn2model_eventdefinitions;


    public BPMN2Model_CatchEvent(
        boolean parallelMultiple    ) {
        super(
        );
        this.parallelMultiple = parallelMultiple;
        this.bpmn2model_eventdefinitions = new ArrayList<>();
        this.bpmn2model_eventdefinitions = new ArrayList<>();
    }

    public BPMN2Model_CatchEvent(
        boolean parallelMultiple        ArrayList<BPMN2Model_EventDefinition> bpmn2model_eventdefinitions,        ArrayList<BPMN2Model_EventDefinition> bpmn2model_eventdefinitions    ) {
        this.parallelMultiple = parallelMultiple;
        this.bpmn2model_eventdefinitions = bpmn2model_eventdefinitions;
        this.bpmn2model_eventdefinitions = bpmn2model_eventdefinitions;
    }

    public boolean getParallelmultiple() {
        return parallelMultiple;
    }

    public void setParallelmultiple(boolean parallelMultiple) {
        this.parallelMultiple = parallelMultiple;
    }

    public List<BPMN2Model_EventDefinition> getBpmn2model_eventdefinitions() {
        return bpmn2model_eventdefinitions;
    }

    public void addBpmn2model_eventdefinition(Bpmn2model_eventdefinition bpmn2model_eventdefinition) {
        this.bpmn2model_eventdefinitions.add(bpmn2model_eventdefinition);
    }
    public BPMN2Model_OutputSet getBpmn2model_outputset() {
        return bpmn2model_outputset;
    }

    public void setBpmn2model_outputset(BPMN2Model_OutputSet bpmn2model_outputset) {
        this.bpmn2model_outputset = bpmn2model_outputset;
    }
    public List<BPMN2Model_EventDefinition> getBpmn2model_eventdefinitions() {
        return bpmn2model_eventdefinitions;
    }

    public void addBpmn2model_eventdefinition(Bpmn2model_eventdefinition bpmn2model_eventdefinition) {
        this.bpmn2model_eventdefinitions.add(bpmn2model_eventdefinition);
    }

}