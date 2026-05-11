





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_BaseElement extends BPMNBase {

    private String anyAttribute;
    private String id;





    private BPMN2Model_Lane bpmn2model_lane;




    private List<BPMN2Model_Documentation> bpmn2model_documentations;




    private BPMN2Model_Lane bpmn2model_lane;




    private BPMN2Model_DocumentRoot bpmn2model_documentroot;




    private BPMN2Model_DocumentRoot bpmn2model_documentroot;




    private List<BPMN2Model_ExtensionAttributeValue> bpmn2model_extensionattributevalues;




    private BPMN2Model_Association bpmn2model_association;




    private BPMN2Model_Association bpmn2model_association;




    private List<BPMN2Model_ExtensionDefinition> bpmn2model_extensiondefinitions;


    public BPMN2Model_BaseElement(
        String anyAttribute,        String id    ) {
        super(
        );
        this.anyAttribute = anyAttribute;
        this.id = id;
        this.bpmn2model_documentations = new ArrayList<>();
        this.bpmn2model_extensionattributevalues = new ArrayList<>();
        this.bpmn2model_extensiondefinitions = new ArrayList<>();
    }

    public BPMN2Model_BaseElement(
        String anyAttribute,        String id        ArrayList<BPMN2Model_Documentation> bpmn2model_documentations,        ArrayList<BPMN2Model_ExtensionAttributeValue> bpmn2model_extensionattributevalues,        ArrayList<BPMN2Model_ExtensionDefinition> bpmn2model_extensiondefinitions    ) {
        this.anyAttribute = anyAttribute;
        this.id = id;
        this.bpmn2model_documentations = bpmn2model_documentations;
        this.bpmn2model_extensionattributevalues = bpmn2model_extensionattributevalues;
        this.bpmn2model_extensiondefinitions = bpmn2model_extensiondefinitions;
    }

    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public BPMN2Model_Lane getBpmn2model_lane() {
        return bpmn2model_lane;
    }

    public void setBpmn2model_lane(BPMN2Model_Lane bpmn2model_lane) {
        this.bpmn2model_lane = bpmn2model_lane;
    }
    public List<BPMN2Model_Documentation> getBpmn2model_documentations() {
        return bpmn2model_documentations;
    }

    public void addBpmn2model_documentation(Bpmn2model_documentation bpmn2model_documentation) {
        this.bpmn2model_documentations.add(bpmn2model_documentation);
    }
    public BPMN2Model_Lane getBpmn2model_lane() {
        return bpmn2model_lane;
    }

    public void setBpmn2model_lane(BPMN2Model_Lane bpmn2model_lane) {
        this.bpmn2model_lane = bpmn2model_lane;
    }
    public BPMN2Model_DocumentRoot getBpmn2model_documentroot() {
        return bpmn2model_documentroot;
    }

    public void setBpmn2model_documentroot(BPMN2Model_DocumentRoot bpmn2model_documentroot) {
        this.bpmn2model_documentroot = bpmn2model_documentroot;
    }
    public BPMN2Model_DocumentRoot getBpmn2model_documentroot() {
        return bpmn2model_documentroot;
    }

    public void setBpmn2model_documentroot(BPMN2Model_DocumentRoot bpmn2model_documentroot) {
        this.bpmn2model_documentroot = bpmn2model_documentroot;
    }
    public List<BPMN2Model_ExtensionAttributeValue> getBpmn2model_extensionattributevalues() {
        return bpmn2model_extensionattributevalues;
    }

    public void addBpmn2model_extensionattributevalue(Bpmn2model_extensionattributevalue bpmn2model_extensionattributevalue) {
        this.bpmn2model_extensionattributevalues.add(bpmn2model_extensionattributevalue);
    }
    public BPMN2Model_Association getBpmn2model_association() {
        return bpmn2model_association;
    }

    public void setBpmn2model_association(BPMN2Model_Association bpmn2model_association) {
        this.bpmn2model_association = bpmn2model_association;
    }
    public BPMN2Model_Association getBpmn2model_association() {
        return bpmn2model_association;
    }

    public void setBpmn2model_association(BPMN2Model_Association bpmn2model_association) {
        this.bpmn2model_association = bpmn2model_association;
    }
    public List<BPMN2Model_ExtensionDefinition> getBpmn2model_extensiondefinitions() {
        return bpmn2model_extensiondefinitions;
    }

    public void addBpmn2model_extensiondefinition(Bpmn2model_extensiondefinition bpmn2model_extensiondefinition) {
        this.bpmn2model_extensiondefinitions.add(bpmn2model_extensiondefinition);
    }

}