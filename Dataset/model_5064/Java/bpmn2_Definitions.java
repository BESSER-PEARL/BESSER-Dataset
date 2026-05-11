





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Definitions extends BaseElement {

    private String expressionLanguage;
    private String exporter;
    private String exporterVersion;
    private String typeLanguage;
    private String targetNamespace;





    private List<bpmn2_RootElement> bpmn2_rootelements;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_Definitions(
        String expressionLanguage,        String exporter,        String exporterVersion,        String typeLanguage,        String targetNamespace    ) {
        super(
        );
        this.expressionLanguage = expressionLanguage;
        this.exporter = exporter;
        this.exporterVersion = exporterVersion;
        this.typeLanguage = typeLanguage;
        this.targetNamespace = targetNamespace;
        this.bpmn2_rootelements = new ArrayList<>();
    }

    public bpmn2_Definitions(
        String expressionLanguage,        String exporter,        String exporterVersion,        String typeLanguage,        String targetNamespace        ArrayList<bpmn2_RootElement> bpmn2_rootelements    ) {
        this.expressionLanguage = expressionLanguage;
        this.exporter = exporter;
        this.exporterVersion = exporterVersion;
        this.typeLanguage = typeLanguage;
        this.targetNamespace = targetNamespace;
        this.bpmn2_rootelements = bpmn2_rootelements;
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

    public List<bpmn2_RootElement> getBpmn2_rootelements() {
        return bpmn2_rootelements;
    }

    public void addBpmn2_rootelement(Bpmn2_rootelement bpmn2_rootelement) {
        this.bpmn2_rootelements.add(bpmn2_rootelement);
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}