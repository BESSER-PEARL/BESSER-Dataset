





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Import  {

    private String location;
    private String namespace;
    private String importType;





    private BPMNProfile_Definitions bpmnprofile_definitions;




    private BPMNProfile_Definitions bpmnprofile_definitions;


    public BPMNProfile_Import(
        String location,        String namespace,        String importType    ) {
        this.location = location;
        this.namespace = namespace;
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
    public String getImporttype() {
        return importType;
    }

    public void setImporttype(String importType) {
        this.importType = importType;
    }

    public BPMNProfile_Definitions getBpmnprofile_definitions() {
        return bpmnprofile_definitions;
    }

    public void setBpmnprofile_definitions(BPMNProfile_Definitions bpmnprofile_definitions) {
        this.bpmnprofile_definitions = bpmnprofile_definitions;
    }
    public BPMNProfile_Definitions getBpmnprofile_definitions() {
        return bpmnprofile_definitions;
    }

    public void setBpmnprofile_definitions(BPMNProfile_Definitions bpmnprofile_definitions) {
        this.bpmnprofile_definitions = bpmnprofile_definitions;
    }

}