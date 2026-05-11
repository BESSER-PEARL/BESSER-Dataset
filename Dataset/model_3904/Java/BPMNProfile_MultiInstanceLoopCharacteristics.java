





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_MultiInstanceLoopCharacteristics extends LoopCharacteristics {

    private String behavior;
    private String isSequential;





    private BPMNProfile_EventDefinition bpmnprofile_eventdefinition;




    private BPMNProfile_ItemAwareElement bpmnprofile_itemawareelement;




    private BPMNProfile_BPMNExpression bpmnprofile_bpmnexpression;




    private BPMNProfile_DataInput bpmnprofile_datainput;




    private List<BPMNProfile_ComplexBehaviorDefinition> bpmnprofile_complexbehaviordefinitions;




    private BPMNProfile_ItemAwareElement bpmnprofile_itemawareelement;




    private BPMNProfile_BPMNExpression bpmnprofile_bpmnexpression;




    private BPMNProfile_EventDefinition bpmnprofile_eventdefinition;




    private BPMNProfile_DataOutput bpmnprofile_dataoutput;


    public BPMNProfile_MultiInstanceLoopCharacteristics(
        String behavior,        String isSequential    ) {
        super(
        );
        this.behavior = behavior;
        this.isSequential = isSequential;
        this.bpmnprofile_complexbehaviordefinitions = new ArrayList<>();
    }

    public BPMNProfile_MultiInstanceLoopCharacteristics(
        String behavior,        String isSequential        ArrayList<BPMNProfile_ComplexBehaviorDefinition> bpmnprofile_complexbehaviordefinitions    ) {
        this.behavior = behavior;
        this.isSequential = isSequential;
        this.bpmnprofile_complexbehaviordefinitions = bpmnprofile_complexbehaviordefinitions;
    }

    public String getBehavior() {
        return behavior;
    }

    public void setBehavior(String behavior) {
        this.behavior = behavior;
    }
    public String getIssequential() {
        return isSequential;
    }

    public void setIssequential(String isSequential) {
        this.isSequential = isSequential;
    }

    public BPMNProfile_EventDefinition getBpmnprofile_eventdefinition() {
        return bpmnprofile_eventdefinition;
    }

    public void setBpmnprofile_eventdefinition(BPMNProfile_EventDefinition bpmnprofile_eventdefinition) {
        this.bpmnprofile_eventdefinition = bpmnprofile_eventdefinition;
    }
    public BPMNProfile_ItemAwareElement getBpmnprofile_itemawareelement() {
        return bpmnprofile_itemawareelement;
    }

    public void setBpmnprofile_itemawareelement(BPMNProfile_ItemAwareElement bpmnprofile_itemawareelement) {
        this.bpmnprofile_itemawareelement = bpmnprofile_itemawareelement;
    }
    public BPMNProfile_BPMNExpression getBpmnprofile_bpmnexpression() {
        return bpmnprofile_bpmnexpression;
    }

    public void setBpmnprofile_bpmnexpression(BPMNProfile_BPMNExpression bpmnprofile_bpmnexpression) {
        this.bpmnprofile_bpmnexpression = bpmnprofile_bpmnexpression;
    }
    public BPMNProfile_DataInput getBpmnprofile_datainput() {
        return bpmnprofile_datainput;
    }

    public void setBpmnprofile_datainput(BPMNProfile_DataInput bpmnprofile_datainput) {
        this.bpmnprofile_datainput = bpmnprofile_datainput;
    }
    public List<BPMNProfile_ComplexBehaviorDefinition> getBpmnprofile_complexbehaviordefinitions() {
        return bpmnprofile_complexbehaviordefinitions;
    }

    public void addBpmnprofile_complexbehaviordefinition(Bpmnprofile_complexbehaviordefinition bpmnprofile_complexbehaviordefinition) {
        this.bpmnprofile_complexbehaviordefinitions.add(bpmnprofile_complexbehaviordefinition);
    }
    public BPMNProfile_ItemAwareElement getBpmnprofile_itemawareelement() {
        return bpmnprofile_itemawareelement;
    }

    public void setBpmnprofile_itemawareelement(BPMNProfile_ItemAwareElement bpmnprofile_itemawareelement) {
        this.bpmnprofile_itemawareelement = bpmnprofile_itemawareelement;
    }
    public BPMNProfile_BPMNExpression getBpmnprofile_bpmnexpression() {
        return bpmnprofile_bpmnexpression;
    }

    public void setBpmnprofile_bpmnexpression(BPMNProfile_BPMNExpression bpmnprofile_bpmnexpression) {
        this.bpmnprofile_bpmnexpression = bpmnprofile_bpmnexpression;
    }
    public BPMNProfile_EventDefinition getBpmnprofile_eventdefinition() {
        return bpmnprofile_eventdefinition;
    }

    public void setBpmnprofile_eventdefinition(BPMNProfile_EventDefinition bpmnprofile_eventdefinition) {
        this.bpmnprofile_eventdefinition = bpmnprofile_eventdefinition;
    }
    public BPMNProfile_DataOutput getBpmnprofile_dataoutput() {
        return bpmnprofile_dataoutput;
    }

    public void setBpmnprofile_dataoutput(BPMNProfile_DataOutput bpmnprofile_dataoutput) {
        this.bpmnprofile_dataoutput = bpmnprofile_dataoutput;
    }

}