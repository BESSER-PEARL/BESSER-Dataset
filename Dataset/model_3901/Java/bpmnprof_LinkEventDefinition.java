





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_LinkEventDefinition extends EventDefinition {






    private List<bpmnprof_LinkEventDefinition> bpmnprof_linkeventdefinitions;




    private bpmnprof_LinkEventDefinition bpmnprof_linkeventdefinition;


    public bpmnprof_LinkEventDefinition(
    ) {
        super(
        );
        this.bpmnprof_linkeventdefinitions = new ArrayList<>();
    }

    public bpmnprof_LinkEventDefinition(
        ArrayList<bpmnprof_LinkEventDefinition> bpmnprof_linkeventdefinitions    ) {
        this.bpmnprof_linkeventdefinitions = bpmnprof_linkeventdefinitions;
    }


    public List<bpmnprof_LinkEventDefinition> getBpmnprof_linkeventdefinitions() {
        return bpmnprof_linkeventdefinitions;
    }

    public void addBpmnprof_linkeventdefinition(Bpmnprof_linkeventdefinition bpmnprof_linkeventdefinition) {
        this.bpmnprof_linkeventdefinitions.add(bpmnprof_linkeventdefinition);
    }
    public bpmnprof_LinkEventDefinition getBpmnprof_linkeventdefinition() {
        return bpmnprof_linkeventdefinition;
    }

    public void setBpmnprof_linkeventdefinition(bpmnprof_LinkEventDefinition bpmnprof_linkeventdefinition) {
        this.bpmnprof_linkeventdefinition = bpmnprof_linkeventdefinition;
    }

}