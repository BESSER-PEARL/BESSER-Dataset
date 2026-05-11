





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ResourceParameter extends BaseElement {

    private String name;
    private boolean isRequired;





    private bpmn2_ItemDefinition bpmn2_itemdefinition;




    private bpmn2_Resource bpmn2_resource;


    public bpmn2_ResourceParameter(
        String name,        boolean isRequired    ) {
        super(
        );
        this.name = name;
        this.isRequired = isRequired;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(boolean isRequired) {
        this.isRequired = isRequired;
    }

    public bpmn2_ItemDefinition getBpmn2_itemdefinition() {
        return bpmn2_itemdefinition;
    }

    public void setBpmn2_itemdefinition(bpmn2_ItemDefinition bpmn2_itemdefinition) {
        this.bpmn2_itemdefinition = bpmn2_itemdefinition;
    }
    public bpmn2_Resource getBpmn2_resource() {
        return bpmn2_resource;
    }

    public void setBpmn2_resource(bpmn2_Resource bpmn2_resource) {
        this.bpmn2_resource = bpmn2_resource;
    }

}