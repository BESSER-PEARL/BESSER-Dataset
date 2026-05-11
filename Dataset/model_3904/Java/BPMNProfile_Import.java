





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Import  {

    private String location;
    private String importType;
    private String namespace;





    private BPMNProfile_Definitions bpmnprofile_definitions;




    private BPMNProfile_Definitions bpmnprofile_definitions;


    public BPMNProfile_Import(
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