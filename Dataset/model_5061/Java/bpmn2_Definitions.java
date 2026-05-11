





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Definitions extends BaseElement {

    private String targetNamespace;
    private String exporterVersion;
    private String typeLanguage;
    private String exporter;
    private String expressionLanguage;
    private String name;





    private List<bpmn2_RootElement> bpmn2_rootelements;


    public bpmn2_Definitions(
        String targetNamespace,        String exporterVersion,        String typeLanguage,        String exporter,        String expressionLanguage,        String name    ) {
        super(
        );
        this.targetNamespace = targetNamespace;
        this.exporterVersion = exporterVersion;
        this.typeLanguage = typeLanguage;
        this.exporter = exporter;
        this.expressionLanguage = expressionLanguage;
        this.name = name;
        this.bpmn2_rootelements = new ArrayList<>();
    }

    public bpmn2_Definitions(
        String targetNamespace,        String exporterVersion,        String typeLanguage,        String exporter,        String expressionLanguage,        String name        ArrayList<bpmn2_RootElement> bpmn2_rootelements    ) {
        this.targetNamespace = targetNamespace;
        this.exporterVersion = exporterVersion;
        this.typeLanguage = typeLanguage;
        this.exporter = exporter;
        this.expressionLanguage = expressionLanguage;
        this.name = name;
        this.bpmn2_rootelements = bpmn2_rootelements;
    }

    public String getTargetnamespace() {
        return targetNamespace;
    }

    public void setTargetnamespace(String targetNamespace) {
        this.targetNamespace = targetNamespace;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bpmn2_RootElement> getBpmn2_rootelements() {
        return bpmn2_rootelements;
    }

    public void addBpmn2_rootelement(Bpmn2_rootelement bpmn2_rootelement) {
        this.bpmn2_rootelements.add(bpmn2_rootelement);
    }

}