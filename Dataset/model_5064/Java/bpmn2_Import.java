





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Import  {

    private String location;
    private String importType;
    private String namespace;





    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Definitions bpmn2_definitions;


    public bpmn2_Import(
        String location,        String importType,        String namespace    ) {
        this.location = location;
        this.importType = importType;
        this.namespace = namespace;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getImporttype() {
        return importType;
    }

    public void setImporttype(String importType) {
        this.importType = importType;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Definitions getBpmn2_definitions() {
        return bpmn2_definitions;
    }

    public void setBpmn2_definitions(bpmn2_Definitions bpmn2_definitions) {
        this.bpmn2_definitions = bpmn2_definitions;
    }

}