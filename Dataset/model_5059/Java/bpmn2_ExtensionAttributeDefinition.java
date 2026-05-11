





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ExtensionAttributeDefinition  {

    private String name;
    private boolean isReference;
    private String type;
    private String id;





    private bpmn2_ExtensionDefinition bpmn2_extensiondefinition;




    private bpmn2_ExtensionDefinition bpmn2_extensiondefinition;




    private bpmn2_ExtensionAttributeValue bpmn2_extensionattributevalue;


    public bpmn2_ExtensionAttributeDefinition(
        String name,        boolean isReference,        String type,        String id    ) {
        this.name = name;
        this.isReference = isReference;
        this.type = type;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsreference() {
        return isReference;
    }

    public void setIsreference(boolean isReference) {
        this.isReference = isReference;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public bpmn2_ExtensionDefinition getBpmn2_extensiondefinition() {
        return bpmn2_extensiondefinition;
    }

    public void setBpmn2_extensiondefinition(bpmn2_ExtensionDefinition bpmn2_extensiondefinition) {
        this.bpmn2_extensiondefinition = bpmn2_extensiondefinition;
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

}