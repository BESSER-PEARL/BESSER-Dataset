





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Definitions extends BaseElement {

    private String typeLanguage;
    private String expressionLanguage;
    private String targetNamespace;
    private String exporter;
    private String exporterVersion;
    private String name;





    private List<bpmn2_Relationship> bpmn2_relationships;




    private List<bpmn2_RootElement> bpmn2_rootelements;


    public bpmn2_Definitions(
        String typeLanguage,        String expressionLanguage,        String targetNamespace,        String exporter,        String exporterVersion,        String name    ) {
        super(
        );
        this.typeLanguage = typeLanguage;
        this.expressionLanguage = expressionLanguage;
        this.targetNamespace = targetNamespace;
        this.exporter = exporter;
        this.exporterVersion = exporterVersion;
        this.name = name;
        this.bpmn2_relationships = new ArrayList<>();
        this.bpmn2_rootelements = new ArrayList<>();
    }

    public bpmn2_Definitions(
        String typeLanguage,        String expressionLanguage,        String targetNamespace,        String exporter,        String exporterVersion,        String name        ArrayList<bpmn2_Relationship> bpmn2_relationships,        ArrayList<bpmn2_RootElement> bpmn2_rootelements    ) {
        this.typeLanguage = typeLanguage;
        this.expressionLanguage = expressionLanguage;
        this.targetNamespace = targetNamespace;
        this.exporter = exporter;
        this.exporterVersion = exporterVersion;
        this.name = name;
        this.bpmn2_relationships = bpmn2_relationships;
        this.bpmn2_rootelements = bpmn2_rootelements;
    }

    public String getTypelanguage() {
        return typeLanguage;
    }

    public void setTypelanguage(String typeLanguage) {
        this.typeLanguage = typeLanguage;
    }
    public String getExpressionlanguage() {
        return expressionLanguage;
    }

    public void setExpressionlanguage(String expressionLanguage) {
        this.expressionLanguage = expressionLanguage;
    }
    public String getTargetnamespace() {
        return targetNamespace;
    }

    public void setTargetnamespace(String targetNamespace) {
        this.targetNamespace = targetNamespace;
    }
    public String getExporter() {
        return exporter;
    }

    public void setExporter(String exporter) {
        this.exporter = exporter;
    }
    public String getExporterversion() {
        return exporterVersion;
    }

    public void setExporterversion(String exporterVersion) {
        this.exporterVersion = exporterVersion;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bpmn2_Relationship> getBpmn2_relationships() {
        return bpmn2_relationships;
    }

    public void addBpmn2_relationship(Bpmn2_relationship bpmn2_relationship) {
        this.bpmn2_relationships.add(bpmn2_relationship);
    }
    public List<bpmn2_RootElement> getBpmn2_rootelements() {
        return bpmn2_rootelements;
    }

    public void addBpmn2_rootelement(Bpmn2_rootelement bpmn2_rootelement) {
        this.bpmn2_rootelements.add(bpmn2_rootelement);
    }

}