





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_Definitions extends BaseElement {

    private String targetNamespace;
    private String typeLanguage;
    private String exporter;
    private String exporterVersion;
    private String expressionLanguage;





    private bpmnprof_BPMNRelationship bpmnprof_bpmnrelationship;




    private List<bpmnprof_BPMNRelationship> bpmnprof_bpmnrelationships;


    public bpmnprof_Definitions(
        String targetNamespace,        String typeLanguage,        String exporter,        String exporterVersion,        String expressionLanguage    ) {
        super(
        );
        this.targetNamespace = targetNamespace;
        this.typeLanguage = typeLanguage;
        this.exporter = exporter;
        this.exporterVersion = exporterVersion;
        this.expressionLanguage = expressionLanguage;
        this.bpmnprof_bpmnrelationships = new ArrayList<>();
    }

    public bpmnprof_Definitions(
        String targetNamespace,        String typeLanguage,        String exporter,        String exporterVersion,        String expressionLanguage        ArrayList<bpmnprof_BPMNRelationship> bpmnprof_bpmnrelationships    ) {
        this.targetNamespace = targetNamespace;
        this.typeLanguage = typeLanguage;
        this.exporter = exporter;
        this.exporterVersion = exporterVersion;
        this.expressionLanguage = expressionLanguage;
        this.bpmnprof_bpmnrelationships = bpmnprof_bpmnrelationships;
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
    public String getExpressionlanguage() {
        return expressionLanguage;
    }

    public void setExpressionlanguage(String expressionLanguage) {
        this.expressionLanguage = expressionLanguage;
    }

    public bpmnprof_BPMNRelationship getBpmnprof_bpmnrelationship() {
        return bpmnprof_bpmnrelationship;
    }

    public void setBpmnprof_bpmnrelationship(bpmnprof_BPMNRelationship bpmnprof_bpmnrelationship) {
        this.bpmnprof_bpmnrelationship = bpmnprof_bpmnrelationship;
    }
    public List<bpmnprof_BPMNRelationship> getBpmnprof_bpmnrelationships() {
        return bpmnprof_bpmnrelationships;
    }

    public void addBpmnprof_bpmnrelationship(Bpmnprof_bpmnrelationship bpmnprof_bpmnrelationship) {
        this.bpmnprof_bpmnrelationships.add(bpmnprof_bpmnrelationship);
    }

}