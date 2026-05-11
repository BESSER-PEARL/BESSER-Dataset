





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Extension extends BPMNBase {

    private boolean mustUnderstand;
    private String xsdDefinition;





    private BPMN2Model_Definitions bpmn2model_definitions;




    private BPMN2Model_ExtensionDefinition bpmn2model_extensiondefinition;




    private BPMN2Model_DocumentRoot bpmn2model_documentroot;


    public BPMN2Model_Extension(
        boolean mustUnderstand,        String xsdDefinition    ) {
        super(
        );
        this.mustUnderstand = mustUnderstand;
        this.xsdDefinition = xsdDefinition;
    }


    public boolean getMustunderstand() {
        return mustUnderstand;
    }

    public void setMustunderstand(boolean mustUnderstand) {
        this.mustUnderstand = mustUnderstand;
    }
    public String getXsddefinition() {
        return xsdDefinition;
    }

    public void setXsddefinition(String xsdDefinition) {
        this.xsdDefinition = xsdDefinition;
    }

    public BPMN2Model_Definitions getBpmn2model_definitions() {
        return bpmn2model_definitions;
    }

    public void setBpmn2model_definitions(BPMN2Model_Definitions bpmn2model_definitions) {
        this.bpmn2model_definitions = bpmn2model_definitions;
    }
    public BPMN2Model_ExtensionDefinition getBpmn2model_extensiondefinition() {
        return bpmn2model_extensiondefinition;
    }

    public void setBpmn2model_extensiondefinition(BPMN2Model_ExtensionDefinition bpmn2model_extensiondefinition) {
        this.bpmn2model_extensiondefinition = bpmn2model_extensiondefinition;
    }
    public BPMN2Model_DocumentRoot getBpmn2model_documentroot() {
        return bpmn2model_documentroot;
    }

    public void setBpmn2model_documentroot(BPMN2Model_DocumentRoot bpmn2model_documentroot) {
        this.bpmn2model_documentroot = bpmn2model_documentroot;
    }

}