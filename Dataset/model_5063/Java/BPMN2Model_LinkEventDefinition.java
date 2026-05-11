





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_LinkEventDefinition extends EventDefinition {

    private String name;





    private BPMN2Model_LinkEventDefinition bpmn2model_linkeventdefinition;




    private List<BPMN2Model_LinkEventDefinition> bpmn2model_linkeventdefinitions;


    public BPMN2Model_LinkEventDefinition(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2model_linkeventdefinitions = new ArrayList<>();
    }

    public BPMN2Model_LinkEventDefinition(
        String name        ArrayList<BPMN2Model_LinkEventDefinition> bpmn2model_linkeventdefinitions    ) {
        this.name = name;
        this.bpmn2model_linkeventdefinitions = bpmn2model_linkeventdefinitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BPMN2Model_LinkEventDefinition getBpmn2model_linkeventdefinition() {
        return bpmn2model_linkeventdefinition;
    }

    public void setBpmn2model_linkeventdefinition(BPMN2Model_LinkEventDefinition bpmn2model_linkeventdefinition) {
        this.bpmn2model_linkeventdefinition = bpmn2model_linkeventdefinition;
    }
    public List<BPMN2Model_LinkEventDefinition> getBpmn2model_linkeventdefinitions() {
        return bpmn2model_linkeventdefinitions;
    }

    public void addBpmn2model_linkeventdefinition(Bpmn2model_linkeventdefinition bpmn2model_linkeventdefinition) {
        this.bpmn2model_linkeventdefinitions.add(bpmn2model_linkeventdefinition);
    }

}