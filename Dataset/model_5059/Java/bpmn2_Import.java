





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Import  {

    private String id;
    private String importType;
    private String location;
    private String namespace;





    private bpmn2_ItemDefinition bpmn2_itemdefinition;




    private bpmn2_Definitions bpmn2_definitions;


    public bpmn2_Import(
        String id,        String importType,        String location,        String namespace    ) {
        this.id = id;
        this.importType = importType;
        this.location = location;
        this.namespace = namespace;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getImporttype() {
        return importType;
    }

    public void setImporttype(String importType) {
        this.importType = importType;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
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