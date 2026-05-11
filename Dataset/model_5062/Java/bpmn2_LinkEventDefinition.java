





import java.util.List;
import java.util.ArrayList;

public class bpmn2_LinkEventDefinition extends EventDefinition {

    private String name;





    private List<bpmn2_LinkEventDefinition> bpmn2_linkeventdefinitions;




    private bpmn2_LinkEventDefinition bpmn2_linkeventdefinition;


    public bpmn2_LinkEventDefinition(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_linkeventdefinitions = new ArrayList<>();
    }

    public bpmn2_LinkEventDefinition(
        String name        ArrayList<bpmn2_LinkEventDefinition> bpmn2_linkeventdefinitions    ) {
        this.name = name;
        this.bpmn2_linkeventdefinitions = bpmn2_linkeventdefinitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bpmn2_LinkEventDefinition> getBpmn2_linkeventdefinitions() {
        return bpmn2_linkeventdefinitions;
    }

    public void addBpmn2_linkeventdefinition(Bpmn2_linkeventdefinition bpmn2_linkeventdefinition) {
        this.bpmn2_linkeventdefinitions.add(bpmn2_linkeventdefinition);
    }
    public bpmn2_LinkEventDefinition getBpmn2_linkeventdefinition() {
        return bpmn2_linkeventdefinition;
    }

    public void setBpmn2_linkeventdefinition(bpmn2_LinkEventDefinition bpmn2_linkeventdefinition) {
        this.bpmn2_linkeventdefinition = bpmn2_linkeventdefinition;
    }

}