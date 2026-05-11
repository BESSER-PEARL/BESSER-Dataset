





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNEvent extends FlowNode, InteractionNode {






    private List<BPMNProfile_BPMNProperty> bpmnprofile_bpmnpropertys;




    private List<BPMNProfile_EventDefinition> bpmnprofile_eventdefinitions;




    private List<BPMNProfile_EventDefinition> bpmnprofile_eventdefinitions;


    public BPMNProfile_BPMNEvent(
    ) {
        super(
        );
        this.bpmnprofile_bpmnpropertys = new ArrayList<>();
        this.bpmnprofile_eventdefinitions = new ArrayList<>();
        this.bpmnprofile_eventdefinitions = new ArrayList<>();
    }

    public BPMNProfile_BPMNEvent(
        ArrayList<BPMNProfile_BPMNProperty> bpmnprofile_bpmnpropertys,        ArrayList<BPMNProfile_EventDefinition> bpmnprofile_eventdefinitions,        ArrayList<BPMNProfile_EventDefinition> bpmnprofile_eventdefinitions    ) {
        this.bpmnprofile_bpmnpropertys = bpmnprofile_bpmnpropertys;
        this.bpmnprofile_eventdefinitions = bpmnprofile_eventdefinitions;
        this.bpmnprofile_eventdefinitions = bpmnprofile_eventdefinitions;
    }


    public List<BPMNProfile_BPMNProperty> getBpmnprofile_bpmnpropertys() {
        return bpmnprofile_bpmnpropertys;
    }

    public void addBpmnprofile_bpmnproperty(Bpmnprofile_bpmnproperty bpmnprofile_bpmnproperty) {
        this.bpmnprofile_bpmnpropertys.add(bpmnprofile_bpmnproperty);
    }
    public List<BPMNProfile_EventDefinition> getBpmnprofile_eventdefinitions() {
        return bpmnprofile_eventdefinitions;
    }

    public void addBpmnprofile_eventdefinition(Bpmnprofile_eventdefinition bpmnprofile_eventdefinition) {
        this.bpmnprofile_eventdefinitions.add(bpmnprofile_eventdefinition);
    }
    public List<BPMNProfile_EventDefinition> getBpmnprofile_eventdefinitions() {
        return bpmnprofile_eventdefinitions;
    }

    public void addBpmnprofile_eventdefinition(Bpmnprofile_eventdefinition bpmnprofile_eventdefinition) {
        this.bpmnprofile_eventdefinitions.add(bpmnprofile_eventdefinition);
    }

}