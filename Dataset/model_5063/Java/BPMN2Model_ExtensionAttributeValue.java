





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ExtensionAttributeValue extends BPMNBase {

    private String value;





    private BPMN2Model_ExtensionAttributeDefinition bpmn2model_extensionattributedefinition;




    private BPMN2Model_DocumentRoot bpmn2model_documentroot;




    private BPMN2Model_EObject bpmn2model_eobject;


    public BPMN2Model_ExtensionAttributeValue(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public BPMN2Model_ExtensionAttributeDefinition getBpmn2model_extensionattributedefinition() {
        return bpmn2model_extensionattributedefinition;
    }

    public void setBpmn2model_extensionattributedefinition(BPMN2Model_ExtensionAttributeDefinition bpmn2model_extensionattributedefinition) {
        this.bpmn2model_extensionattributedefinition = bpmn2model_extensionattributedefinition;
    }
    public BPMN2Model_DocumentRoot getBpmn2model_documentroot() {
        return bpmn2model_documentroot;
    }

    public void setBpmn2model_documentroot(BPMN2Model_DocumentRoot bpmn2model_documentroot) {
        this.bpmn2model_documentroot = bpmn2model_documentroot;
    }
    public BPMN2Model_EObject getBpmn2model_eobject() {
        return bpmn2model_eobject;
    }

    public void setBpmn2model_eobject(BPMN2Model_EObject bpmn2model_eobject) {
        this.bpmn2model_eobject = bpmn2model_eobject;
    }

}