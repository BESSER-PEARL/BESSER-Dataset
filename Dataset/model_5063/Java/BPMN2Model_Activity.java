





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Activity extends FlowNode {

    private int startQuantity;
    private int completionQuantity;
    private boolean isForCompensation;





    private BPMN2Model_SequenceFlow bpmn2model_sequenceflow;




    private BPMN2Model_LoopCharacteristics bpmn2model_loopcharacteristics;




    private List<BPMN2Model_Property> bpmn2model_propertys;


    public BPMN2Model_Activity(
        int startQuantity,        int completionQuantity,        boolean isForCompensation    ) {
        super(
        );
        this.startQuantity = startQuantity;
        this.completionQuantity = completionQuantity;
        this.isForCompensation = isForCompensation;
        this.bpmn2model_propertys = new ArrayList<>();
    }

    public BPMN2Model_Activity(
        int startQuantity,        int completionQuantity,        boolean isForCompensation        ArrayList<BPMN2Model_Property> bpmn2model_propertys    ) {
        this.startQuantity = startQuantity;
        this.completionQuantity = completionQuantity;
        this.isForCompensation = isForCompensation;
        this.bpmn2model_propertys = bpmn2model_propertys;
    }

    public int getStartquantity() {
        return startQuantity;
    }

    public void setStartquantity(int startQuantity) {
        this.startQuantity = startQuantity;
    }
    public int getCompletionquantity() {
        return completionQuantity;
    }

    public void setCompletionquantity(int completionQuantity) {
        this.completionQuantity = completionQuantity;
    }
    public boolean getIsforcompensation() {
        return isForCompensation;
    }

    public void setIsforcompensation(boolean isForCompensation) {
        this.isForCompensation = isForCompensation;
    }

    public BPMN2Model_SequenceFlow getBpmn2model_sequenceflow() {
        return bpmn2model_sequenceflow;
    }

    public void setBpmn2model_sequenceflow(BPMN2Model_SequenceFlow bpmn2model_sequenceflow) {
        this.bpmn2model_sequenceflow = bpmn2model_sequenceflow;
    }
    public BPMN2Model_LoopCharacteristics getBpmn2model_loopcharacteristics() {
        return bpmn2model_loopcharacteristics;
    }

    public void setBpmn2model_loopcharacteristics(BPMN2Model_LoopCharacteristics bpmn2model_loopcharacteristics) {
        this.bpmn2model_loopcharacteristics = bpmn2model_loopcharacteristics;
    }
    public List<BPMN2Model_Property> getBpmn2model_propertys() {
        return bpmn2model_propertys;
    }

    public void addBpmn2model_property(Bpmn2model_property bpmn2model_property) {
        this.bpmn2model_propertys.add(bpmn2model_property);
    }

}