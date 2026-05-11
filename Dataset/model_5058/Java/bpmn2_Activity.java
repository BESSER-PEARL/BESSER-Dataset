





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Activity extends InteractionNode, FlowNode {

    private int startQuantity;
    private int completionQuantity;
    private boolean isForCompensation;





    private bpmn2_LoopCharacteristics bpmn2_loopcharacteristics;




    private bpmn2_SequenceFlow bpmn2_sequenceflow;




    private bpmn2_InputOutputSpecification bpmn2_inputoutputspecification;




    private List<bpmn2_Property> bpmn2_propertys;




    private List<bpmn2_ResourceRole> bpmn2_resourceroles;


    public bpmn2_Activity(
        int startQuantity,        int completionQuantity,        boolean isForCompensation    ) {
        super(
        );
        this.startQuantity = startQuantity;
        this.completionQuantity = completionQuantity;
        this.isForCompensation = isForCompensation;
        this.bpmn2_propertys = new ArrayList<>();
        this.bpmn2_resourceroles = new ArrayList<>();
    }

    public bpmn2_Activity(
        int startQuantity,        int completionQuantity,        boolean isForCompensation        ArrayList<bpmn2_Property> bpmn2_propertys,        ArrayList<bpmn2_ResourceRole> bpmn2_resourceroles    ) {
        this.startQuantity = startQuantity;
        this.completionQuantity = completionQuantity;
        this.isForCompensation = isForCompensation;
        this.bpmn2_propertys = bpmn2_propertys;
        this.bpmn2_resourceroles = bpmn2_resourceroles;
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

    public bpmn2_LoopCharacteristics getBpmn2_loopcharacteristics() {
        return bpmn2_loopcharacteristics;
    }

    public void setBpmn2_loopcharacteristics(bpmn2_LoopCharacteristics bpmn2_loopcharacteristics) {
        this.bpmn2_loopcharacteristics = bpmn2_loopcharacteristics;
    }
    public bpmn2_SequenceFlow getBpmn2_sequenceflow() {
        return bpmn2_sequenceflow;
    }

    public void setBpmn2_sequenceflow(bpmn2_SequenceFlow bpmn2_sequenceflow) {
        this.bpmn2_sequenceflow = bpmn2_sequenceflow;
    }
    public bpmn2_InputOutputSpecification getBpmn2_inputoutputspecification() {
        return bpmn2_inputoutputspecification;
    }

    public void setBpmn2_inputoutputspecification(bpmn2_InputOutputSpecification bpmn2_inputoutputspecification) {
        this.bpmn2_inputoutputspecification = bpmn2_inputoutputspecification;
    }
    public List<bpmn2_Property> getBpmn2_propertys() {
        return bpmn2_propertys;
    }

    public void addBpmn2_property(Bpmn2_property bpmn2_property) {
        this.bpmn2_propertys.add(bpmn2_property);
    }
    public List<bpmn2_ResourceRole> getBpmn2_resourceroles() {
        return bpmn2_resourceroles;
    }

    public void addBpmn2_resourcerole(Bpmn2_resourcerole bpmn2_resourcerole) {
        this.bpmn2_resourceroles.add(bpmn2_resourcerole);
    }

}