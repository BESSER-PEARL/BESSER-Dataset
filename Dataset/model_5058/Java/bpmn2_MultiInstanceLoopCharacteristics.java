





import java.util.List;
import java.util.ArrayList;

public class bpmn2_MultiInstanceLoopCharacteristics extends LoopCharacteristics {

    private String behavior;
    private boolean isSequential;





    private bpmn2_ItemAwareElement bpmn2_itemawareelement;




    private bpmn2_DataInput bpmn2_datainput;




    private bpmn2_ItemAwareElement bpmn2_itemawareelement;




    private bpmn2_Expression bpmn2_expression;




    private bpmn2_EventDefinition bpmn2_eventdefinition;




    private List<bpmn2_ComplexBehaviorDefinition> bpmn2_complexbehaviordefinitions;




    private bpmn2_DataOutput bpmn2_dataoutput;




    private bpmn2_EventDefinition bpmn2_eventdefinition;




    private bpmn2_Expression bpmn2_expression;


    public bpmn2_MultiInstanceLoopCharacteristics(
        String behavior,        boolean isSequential    ) {
        super(
        );
        this.behavior = behavior;
        this.isSequential = isSequential;
        this.bpmn2_complexbehaviordefinitions = new ArrayList<>();
    }

    public bpmn2_MultiInstanceLoopCharacteristics(
        String behavior,        boolean isSequential        ArrayList<bpmn2_ComplexBehaviorDefinition> bpmn2_complexbehaviordefinitions    ) {
        this.behavior = behavior;
        this.isSequential = isSequential;
        this.bpmn2_complexbehaviordefinitions = bpmn2_complexbehaviordefinitions;
    }

    public String getBehavior() {
        return behavior;
    }

    public void setBehavior(String behavior) {
        this.behavior = behavior;
    }
    public boolean getIssequential() {
        return isSequential;
    }

    public void setIssequential(boolean isSequential) {
        this.isSequential = isSequential;
    }

    public bpmn2_ItemAwareElement getBpmn2_itemawareelement() {
        return bpmn2_itemawareelement;
    }

    public void setBpmn2_itemawareelement(bpmn2_ItemAwareElement bpmn2_itemawareelement) {
        this.bpmn2_itemawareelement = bpmn2_itemawareelement;
    }
    public bpmn2_DataInput getBpmn2_datainput() {
        return bpmn2_datainput;
    }

    public void setBpmn2_datainput(bpmn2_DataInput bpmn2_datainput) {
        this.bpmn2_datainput = bpmn2_datainput;
    }
    public bpmn2_ItemAwareElement getBpmn2_itemawareelement() {
        return bpmn2_itemawareelement;
    }

    public void setBpmn2_itemawareelement(bpmn2_ItemAwareElement bpmn2_itemawareelement) {
        this.bpmn2_itemawareelement = bpmn2_itemawareelement;
    }
    public bpmn2_Expression getBpmn2_expression() {
        return bpmn2_expression;
    }

    public void setBpmn2_expression(bpmn2_Expression bpmn2_expression) {
        this.bpmn2_expression = bpmn2_expression;
    }
    public bpmn2_EventDefinition getBpmn2_eventdefinition() {
        return bpmn2_eventdefinition;
    }

    public void setBpmn2_eventdefinition(bpmn2_EventDefinition bpmn2_eventdefinition) {
        this.bpmn2_eventdefinition = bpmn2_eventdefinition;
    }
    public List<bpmn2_ComplexBehaviorDefinition> getBpmn2_complexbehaviordefinitions() {
        return bpmn2_complexbehaviordefinitions;
    }

    public void addBpmn2_complexbehaviordefinition(Bpmn2_complexbehaviordefinition bpmn2_complexbehaviordefinition) {
        this.bpmn2_complexbehaviordefinitions.add(bpmn2_complexbehaviordefinition);
    }
    public bpmn2_DataOutput getBpmn2_dataoutput() {
        return bpmn2_dataoutput;
    }

    public void setBpmn2_dataoutput(bpmn2_DataOutput bpmn2_dataoutput) {
        this.bpmn2_dataoutput = bpmn2_dataoutput;
    }
    public bpmn2_EventDefinition getBpmn2_eventdefinition() {
        return bpmn2_eventdefinition;
    }

    public void setBpmn2_eventdefinition(bpmn2_EventDefinition bpmn2_eventdefinition) {
        this.bpmn2_eventdefinition = bpmn2_eventdefinition;
    }
    public bpmn2_Expression getBpmn2_expression() {
        return bpmn2_expression;
    }

    public void setBpmn2_expression(bpmn2_Expression bpmn2_expression) {
        this.bpmn2_expression = bpmn2_expression;
    }

}