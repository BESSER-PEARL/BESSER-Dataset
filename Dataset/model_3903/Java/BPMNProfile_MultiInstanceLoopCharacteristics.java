





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_MultiInstanceLoopCharacteristics extends LoopCharacteristics {

    private String isSequential;
    private String behavior;





    private BPMNProfile_EventDefinition bpmnprofile_eventdefinition;




    private BPMNProfile_EventDefinition bpmnprofile_eventdefinition;




    private List<BPMNProfile_ComplexBehaviorDefinition> bpmnprofile_complexbehaviordefinitions;


    public BPMNProfile_MultiInstanceLoopCharacteristics(
        String isSequential,        String behavior    ) {
        super(
        );
        this.isSequential = isSequential;
        this.behavior = behavior;
        this.bpmnprofile_complexbehaviordefinitions = new ArrayList<>();
    }

    public BPMNProfile_MultiInstanceLoopCharacteristics(
        String isSequential,        String behavior        ArrayList<BPMNProfile_ComplexBehaviorDefinition> bpmnprofile_complexbehaviordefinitions    ) {
        this.isSequential = isSequential;
        this.behavior = behavior;
        this.bpmnprofile_complexbehaviordefinitions = bpmnprofile_complexbehaviordefinitions;
    }

    public String getIssequential() {
        return isSequential;
    }

    public void setIssequential(String isSequential) {
        this.isSequential = isSequential;
    }
    public String getBehavior() {
        return behavior;
    }

    public void setBehavior(String behavior) {
        this.behavior = behavior;
    }

    public BPMNProfile_EventDefinition getBpmnprofile_eventdefinition() {
        return bpmnprofile_eventdefinition;
    }

    public void setBpmnprofile_eventdefinition(BPMNProfile_EventDefinition bpmnprofile_eventdefinition) {
        this.bpmnprofile_eventdefinition = bpmnprofile_eventdefinition;
    }
    public BPMNProfile_EventDefinition getBpmnprofile_eventdefinition() {
        return bpmnprofile_eventdefinition;
    }

    public void setBpmnprofile_eventdefinition(BPMNProfile_EventDefinition bpmnprofile_eventdefinition) {
        this.bpmnprofile_eventdefinition = bpmnprofile_eventdefinition;
    }
    public List<BPMNProfile_ComplexBehaviorDefinition> getBpmnprofile_complexbehaviordefinitions() {
        return bpmnprofile_complexbehaviordefinitions;
    }

    public void addBpmnprofile_complexbehaviordefinition(Bpmnprofile_complexbehaviordefinition bpmnprofile_complexbehaviordefinition) {
        this.bpmnprofile_complexbehaviordefinitions.add(bpmnprofile_complexbehaviordefinition);
    }

}