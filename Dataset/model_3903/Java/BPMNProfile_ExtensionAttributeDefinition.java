





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ExtensionAttributeDefinition  {

    private String type;
    private String isReference;





    private BPMNProfile_ExtensionDefinition bpmnprofile_extensiondefinition;


    public BPMNProfile_ExtensionAttributeDefinition(
        String type,        String isReference    ) {
        this.type = type;
        this.isReference = isReference;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIsreference() {
        return isReference;
    }

    public void setIsreference(String isReference) {
        this.isReference = isReference;
    }

    public BPMNProfile_ExtensionDefinition getBpmnprofile_extensiondefinition() {
        return bpmnprofile_extensiondefinition;
    }

    public void setBpmnprofile_extensiondefinition(BPMNProfile_ExtensionDefinition bpmnprofile_extensiondefinition) {
        this.bpmnprofile_extensiondefinition = bpmnprofile_extensiondefinition;
    }

}