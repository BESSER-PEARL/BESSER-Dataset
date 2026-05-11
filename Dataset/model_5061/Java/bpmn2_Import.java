





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Import  {

    private String namespace;
    private String importType;
    private String id;
    private String location;





    private bpmn2_ItemDefinition bpmn2_itemdefinition;




    private bpmn2_Definitions bpmn2_definitions;


    public bpmn2_Import(
        String namespace,        String importType,        String id,        String location    ) {
        this.namespace = namespace;
        this.importType = importType;
        this.id = id;
        this.location = location;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getImporttype() {
        return importType;
    }

    public void setImporttype(String importType) {
        this.importType = importType;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public bpmn2_ItemDefinition getBpmn2_itemdefinition() {
        return bpmn2_itemdefinition;
    }

    public void setBpmn2_itemdefinition(bpmn2_ItemDefinition bpmn2_itemdefinition) {
        this.bpmn2_itemdefinition = bpmn2_itemdefinition;
    }
    public bpmn2_Definitions getBpmn2_definitions() {
        return bpmn2_definitions;
    }

    public void setBpmn2_definitions(bpmn2_Definitions bpmn2_definitions) {
        this.bpmn2_definitions = bpmn2_definitions;
    }

}