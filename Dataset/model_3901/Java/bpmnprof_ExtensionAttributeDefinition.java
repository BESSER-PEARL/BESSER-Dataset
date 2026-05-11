





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_ExtensionAttributeDefinition  {

    private String type;
    private String isReference;





    private bpmnprof_ExtensionAttributeValue bpmnprof_extensionattributevalue;




    private bpmnprof_ExtensionDefinition bpmnprof_extensiondefinition;


    public bpmnprof_ExtensionAttributeDefinition(
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

    public bpmnprof_ExtensionAttributeValue getBpmnprof_extensionattributevalue() {
        return bpmnprof_extensionattributevalue;
    }

    public void setBpmnprof_extensionattributevalue(bpmnprof_ExtensionAttributeValue bpmnprof_extensionattributevalue) {
        this.bpmnprof_extensionattributevalue = bpmnprof_extensionattributevalue;
    }
    public bpmnprof_ExtensionDefinition getBpmnprof_extensiondefinition() {
        return bpmnprof_extensiondefinition;
    }

    public void setBpmnprof_extensiondefinition(bpmnprof_ExtensionDefinition bpmnprof_extensiondefinition) {
        this.bpmnprof_extensiondefinition = bpmnprof_extensiondefinition;
    }

}