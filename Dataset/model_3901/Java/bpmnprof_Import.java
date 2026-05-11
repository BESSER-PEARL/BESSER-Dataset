





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_Import  {

    private String namespace;
    private String location;
    private String importType;





    private bpmnprof_Definitions bpmnprof_definitions;




    private bpmnprof_Definitions bpmnprof_definitions;


    public bpmnprof_Import(
        String namespace,        String location,        String importType    ) {
        this.namespace = namespace;
        this.location = location;
        this.importType = importType;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
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

    public bpmnprof_Definitions getBpmnprof_definitions() {
        return bpmnprof_definitions;
    }

    public void setBpmnprof_definitions(bpmnprof_Definitions bpmnprof_definitions) {
        this.bpmnprof_definitions = bpmnprof_definitions;
    }
    public bpmnprof_Definitions getBpmnprof_definitions() {
        return bpmnprof_definitions;
    }

    public void setBpmnprof_definitions(bpmnprof_Definitions bpmnprof_definitions) {
        this.bpmnprof_definitions = bpmnprof_definitions;
    }

}