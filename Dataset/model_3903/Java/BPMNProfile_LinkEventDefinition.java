





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_LinkEventDefinition extends EventDefinition {






    private BPMNProfile_LinkEventDefinition bpmnprofile_linkeventdefinition;




    private List<BPMNProfile_LinkEventDefinition> bpmnprofile_linkeventdefinitions;


    public BPMNProfile_LinkEventDefinition(
    ) {
        super(
        );
        this.bpmnprofile_linkeventdefinitions = new ArrayList<>();
    }

    public BPMNProfile_LinkEventDefinition(
        ArrayList<BPMNProfile_LinkEventDefinition> bpmnprofile_linkeventdefinitions    ) {
        this.bpmnprofile_linkeventdefinitions = bpmnprofile_linkeventdefinitions;
    }


    public BPMNProfile_LinkEventDefinition getBpmnprofile_linkeventdefinition() {
        return bpmnprofile_linkeventdefinition;
    }

    public void setBpmnprofile_linkeventdefinition(BPMNProfile_LinkEventDefinition bpmnprofile_linkeventdefinition) {
        this.bpmnprofile_linkeventdefinition = bpmnprofile_linkeventdefinition;
    }
    public List<BPMNProfile_LinkEventDefinition> getBpmnprofile_linkeventdefinitions() {
        return bpmnprofile_linkeventdefinitions;
    }

    public void addBpmnprofile_linkeventdefinition(Bpmnprofile_linkeventdefinition bpmnprofile_linkeventdefinition) {
        this.bpmnprofile_linkeventdefinitions.add(bpmnprofile_linkeventdefinition);
    }

}