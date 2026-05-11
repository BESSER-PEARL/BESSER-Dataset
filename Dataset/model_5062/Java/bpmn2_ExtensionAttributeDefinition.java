





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ExtensionAttributeDefinition  {

    private String name;
    private String type;
    private boolean isReference;





    private bpmn2_ExtensionDefinition bpmn2_extensiondefinition;




    private bpmn2_ExtensionAttributeValue bpmn2_extensionattributevalue;




    private bpmn2_ExtensionDefinition bpmn2_extensiondefinition;


    public bpmn2_ExtensionAttributeDefinition(
        String name,        String type,        boolean isReference    ) {
        this.name = name;
        this.type = type;
        this.isReference = isReference;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getIsreference() {
        return isReference;
    }

    public void setIsreference(boolean isReference) {
        this.isReference = isReference;
    }

    public bpmn2_ExtensionDefinition getBpmn2_extensiondefinition() {
        return bpmn2_extensiondefinition;
    }

    public void setBpmn2_extensiondefinition(bpmn2_ExtensionDefinition bpmn2_extensiondefinition) {
        this.bpmn2_extensiondefinition = bpmn2_extensiondefinition;
    }
    public bpmn2_ExtensionAttributeValue getBpmn2_extensionattributevalue() {
        return bpmn2_extensionattributevalue;
    }

    public void setBpmn2_extensionattributevalue(bpmn2_ExtensionAttributeValue bpmn2_extensionattributevalue) {
        this.bpmn2_extensionattributevalue = bpmn2_extensionattributevalue;
    }
    public bpmn2_ExtensionDefinition getBpmn2_extensiondefinition() {
        return bpmn2_extensiondefinition;
    }

    public void setBpmn2_extensiondefinition(bpmn2_ExtensionDefinition bpmn2_extensiondefinition) {
        this.bpmn2_extensiondefinition = bpmn2_extensiondefinition;
    }

}