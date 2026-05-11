





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ResourceParameter extends BaseElement {

    private boolean isRequired;
    private String name;





    private BPMN2Model_ItemDefinition bpmn2model_itemdefinition;




    private BPMN2Model_Resource bpmn2model_resource;


    public BPMN2Model_ResourceParameter(
        boolean isRequired,        String name    ) {
        super(
        );
        this.isRequired = isRequired;
        this.name = name;
    }


    public boolean getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(boolean isRequired) {
        this.isRequired = isRequired;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BPMN2Model_ItemDefinition getBpmn2model_itemdefinition() {
        return bpmn2model_itemdefinition;
    }

    public void setBpmn2model_itemdefinition(BPMN2Model_ItemDefinition bpmn2model_itemdefinition) {
        this.bpmn2model_itemdefinition = bpmn2model_itemdefinition;
    }
    public BPMN2Model_Resource getBpmn2model_resource() {
        return bpmn2model_resource;
    }

    public void setBpmn2model_resource(BPMN2Model_Resource bpmn2model_resource) {
        this.bpmn2model_resource = bpmn2model_resource;
    }

}