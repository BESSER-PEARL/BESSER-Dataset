





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ExtensionAttributeDefinition extends BPMNBase {

    private String type;
    private String name;
    private boolean isReference;





    private BPMN2Model_ExtensionDefinition bpmn2model_extensiondefinition;




    private BPMN2Model_ExtensionDefinition bpmn2model_extensiondefinition;


    public BPMN2Model_ExtensionAttributeDefinition(
        String type,        String name,        boolean isReference    ) {
        super(
        );
        this.type = type;
        this.name = name;
        this.isReference = isReference;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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

    public BPMN2Model_ExtensionDefinition getBpmn2model_extensiondefinition() {
        return bpmn2model_extensiondefinition;
    }

    public void setBpmn2model_extensiondefinition(BPMN2Model_ExtensionDefinition bpmn2model_extensiondefinition) {
        this.bpmn2model_extensiondefinition = bpmn2model_extensiondefinition;
    }
    public BPMN2Model_ExtensionDefinition getBpmn2model_extensiondefinition() {
        return bpmn2model_extensiondefinition;
    }

    public void setBpmn2model_extensiondefinition(BPMN2Model_ExtensionDefinition bpmn2model_extensiondefinition) {
        this.bpmn2model_extensiondefinition = bpmn2model_extensiondefinition;
    }

}