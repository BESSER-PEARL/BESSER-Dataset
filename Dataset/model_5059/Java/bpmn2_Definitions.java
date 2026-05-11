





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Definitions extends BaseElement {

    private String exporterVersion;
    private String targetNamespace;
    private String name;
    private String exporter;
    private String expressionLanguage;
    private String typeLanguage;





    private List<bpmn2_RootElement> bpmn2_rootelements;




    private List<bpmn2_Relationship> bpmn2_relationships;


    public bpmn2_Definitions(
        String exporterVersion,        String targetNamespace,        String name,        String exporter,        String expressionLanguage,        String typeLanguage    ) {
        super(
        );
        this.exporterVersion = exporterVersion;
        this.targetNamespace = targetNamespace;
        this.name = name;
        this.exporter = exporter;
        this.expressionLanguage = expressionLanguage;
        this.typeLanguage = typeLanguage;
        this.bpmn2_rootelements = new ArrayList<>();
        this.bpmn2_relationships = new ArrayList<>();
    }

    public bpmn2_Definitions(
        String exporterVersion,        String targetNamespace,        String name,        String exporter,        String expressionLanguage,        String typeLanguage        ArrayList<bpmn2_RootElement> bpmn2_rootelements,        ArrayList<bpmn2_Relationship> bpmn2_relationships    ) {
        this.exporterVersion = exporterVersion;
        this.targetNamespace = targetNamespace;
        this.name = name;
        this.exporter = exporter;
        this.expressionLanguage = expressionLanguage;
        this.typeLanguage = typeLanguage;
        this.bpmn2_rootelements = bpmn2_rootelements;
        this.bpmn2_relationships = bpmn2_relationships;
    }

    public String getExporterversion() {
        return exporterVersion;
    }

    public void setExporterversion(String exporterVersion) {
        this.exporterVersion = exporterVersion;
    }
    public String getTargetnamespace() {
        return targetNamespace;
    }

    public void setTargetnamespace(String targetNamespace) {
        this.targetNamespace = targetNamespace;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExporter() {
        return exporter;
    }

    public void setExporter(String exporter) {
        this.exporter = exporter;
    }
    public String getExpressionlanguage() {
        return expressionLanguage;
    }

    public void setExpressionlanguage(String expressionLanguage) {
        this.expressionLanguage = expressionLanguage;
    }
    public String getTypelanguage() {
        return typeLanguage;
    }

    public void setTypelanguage(String typeLanguage) {
        this.typeLanguage = typeLanguage;
    }

    public List<bpmn2_RootElement> getBpmn2_rootelements() {
        return bpmn2_rootelements;
    }

    public void addBpmn2_rootelement(Bpmn2_rootelement bpmn2_rootelement) {
        this.bpmn2_rootelements.add(bpmn2_rootelement);
    }
    public List<bpmn2_Relationship> getBpmn2_relationships() {
        return bpmn2_relationships;
    }

    public void addBpmn2_relationship(Bpmn2_relationship bpmn2_relationship) {
        this.bpmn2_relationships.add(bpmn2_relationship);
    }

}