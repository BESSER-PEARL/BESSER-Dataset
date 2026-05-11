





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Definitions extends BaseElement {

    private String name;
    private String exporter;
    private String targetNamespace;
    private String typeLanguage;
    private String exporterVersion;
    private String expressionLanguage;





    private List<bpmn2_RootElement> bpmn2_rootelements;




    private List<bpmn2_Relationship> bpmn2_relationships;


    public bpmn2_Definitions(
        String name,        String exporter,        String targetNamespace,        String typeLanguage,        String exporterVersion,        String expressionLanguage    ) {
        super(
        );
        this.name = name;
        this.exporter = exporter;
        this.targetNamespace = targetNamespace;
        this.typeLanguage = typeLanguage;
        this.exporterVersion = exporterVersion;
        this.expressionLanguage = expressionLanguage;
        this.bpmn2_rootelements = new ArrayList<>();
        this.bpmn2_relationships = new ArrayList<>();
    }

    public bpmn2_Definitions(
        String name,        String exporter,        String targetNamespace,        String typeLanguage,        String exporterVersion,        String expressionLanguage        ArrayList<bpmn2_RootElement> bpmn2_rootelements,        ArrayList<bpmn2_Relationship> bpmn2_relationships    ) {
        this.name = name;
        this.exporter = exporter;
        this.targetNamespace = targetNamespace;
        this.typeLanguage = typeLanguage;
        this.exporterVersion = exporterVersion;
        this.expressionLanguage = expressionLanguage;
        this.bpmn2_rootelements = bpmn2_rootelements;
        this.bpmn2_relationships = bpmn2_relationships;
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
    public String getTargetnamespace() {
        return targetNamespace;
    }

    public void setTargetnamespace(String targetNamespace) {
        this.targetNamespace = targetNamespace;
    }
    public String getTypelanguage() {
        return typeLanguage;
    }

    public void setTypelanguage(String typeLanguage) {
        this.typeLanguage = typeLanguage;
    }
    public String getExporterversion() {
        return exporterVersion;
    }

    public void setExporterversion(String exporterVersion) {
        this.exporterVersion = exporterVersion;
    }
    public String getExpressionlanguage() {
        return expressionLanguage;
    }

    public void setExpressionlanguage(String expressionLanguage) {
        this.expressionLanguage = expressionLanguage;
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