





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Definitions extends BaseElement {

    private String name;
    private String exporterVersion;
    private String typeLanguage;
    private String targetNamespace;
    private String expressionLanguage;
    private String exporter;





    private List<BPMN2Model_Relationship> bpmn2model_relationships;




    private List<BPMN2Model_RootElement> bpmn2model_rootelements;


    public BPMN2Model_Definitions(
        String name,        String exporterVersion,        String typeLanguage,        String targetNamespace,        String expressionLanguage,        String exporter    ) {
        super(
        );
        this.name = name;
        this.exporterVersion = exporterVersion;
        this.typeLanguage = typeLanguage;
        this.targetNamespace = targetNamespace;
        this.expressionLanguage = expressionLanguage;
        this.exporter = exporter;
        this.bpmn2model_relationships = new ArrayList<>();
        this.bpmn2model_rootelements = new ArrayList<>();
    }

    public BPMN2Model_Definitions(
        String name,        String exporterVersion,        String typeLanguage,        String targetNamespace,        String expressionLanguage,        String exporter        ArrayList<BPMN2Model_Relationship> bpmn2model_relationships,        ArrayList<BPMN2Model_RootElement> bpmn2model_rootelements    ) {
        this.name = name;
        this.exporterVersion = exporterVersion;
        this.typeLanguage = typeLanguage;
        this.targetNamespace = targetNamespace;
        this.expressionLanguage = expressionLanguage;
        this.exporter = exporter;
        this.bpmn2model_relationships = bpmn2model_relationships;
        this.bpmn2model_rootelements = bpmn2model_rootelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExporterversion() {
        return exporterVersion;
    }

    public void setExporterversion(String exporterVersion) {
        this.exporterVersion = exporterVersion;
    }
    public String getTypelanguage() {
        return typeLanguage;
    }

    public void setTypelanguage(String typeLanguage) {
        this.typeLanguage = typeLanguage;
    }
    public String getTargetnamespace() {
        return targetNamespace;
    }

    public void setTargetnamespace(String targetNamespace) {
        this.targetNamespace = targetNamespace;
    }
    public String getExpressionlanguage() {
        return expressionLanguage;
    }

    public void setExpressionlanguage(String expressionLanguage) {
        this.expressionLanguage = expressionLanguage;
    }
    public String getExporter() {
        return exporter;
    }

    public void setExporter(String exporter) {
        this.exporter = exporter;
    }

    public List<BPMN2Model_Relationship> getBpmn2model_relationships() {
        return bpmn2model_relationships;
    }

    public void addBpmn2model_relationship(Bpmn2model_relationship bpmn2model_relationship) {
        this.bpmn2model_relationships.add(bpmn2model_relationship);
    }
    public List<BPMN2Model_RootElement> getBpmn2model_rootelements() {
        return bpmn2model_rootelements;
    }

    public void addBpmn2model_rootelement(Bpmn2model_rootelement bpmn2model_rootelement) {
        this.bpmn2model_rootelements.add(bpmn2model_rootelement);
    }

}