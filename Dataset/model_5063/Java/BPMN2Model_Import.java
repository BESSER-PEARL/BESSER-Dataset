





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Import extends BPMNBase {

    private String namespace;
    private String importType;
    private String location;





    private BPMN2Model_ItemDefinition bpmn2model_itemdefinition;




    private BPMN2Model_Definitions bpmn2model_definitions;




    private BPMN2Model_DocumentRoot bpmn2model_documentroot;


    public BPMN2Model_Import(
        String namespace,        String importType,        String location    ) {
        super(
        );
        this.namespace = namespace;
        this.importType = importType;
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
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public BPMN2Model_ItemDefinition getBpmn2model_itemdefinition() {
        return bpmn2model_itemdefinition;
    }

    public void setBpmn2model_itemdefinition(BPMN2Model_ItemDefinition bpmn2model_itemdefinition) {
        this.bpmn2model_itemdefinition = bpmn2model_itemdefinition;
    }
    public BPMN2Model_Definitions getBpmn2model_definitions() {
        return bpmn2model_definitions;
    }

    public void setBpmn2model_definitions(BPMN2Model_Definitions bpmn2model_definitions) {
        this.bpmn2model_definitions = bpmn2model_definitions;
    }
    public BPMN2Model_DocumentRoot getBpmn2model_documentroot() {
        return bpmn2model_documentroot;
    }

    public void setBpmn2model_documentroot(BPMN2Model_DocumentRoot bpmn2model_documentroot) {
        this.bpmn2model_documentroot = bpmn2model_documentroot;
    }

}