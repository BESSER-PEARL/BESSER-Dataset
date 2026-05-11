





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Definitions extends BaseElement {

    private String exporter;
    private String exporterVersion;
    private String expressionLanguage;
    private String targetNamespace;
    private String typeLanguage;





    private BPMNProfile_RootElement bpmnprofile_rootelement;




    private List<BPMNProfile_RootElement> bpmnprofile_rootelements;


    public BPMNProfile_Definitions(
        String exporter,        String exporterVersion,        String expressionLanguage,        String targetNamespace,        String typeLanguage    ) {
        super(
        );
        this.exporter = exporter;
        this.exporterVersion = exporterVersion;
        this.expressionLanguage = expressionLanguage;
        this.targetNamespace = targetNamespace;
        this.typeLanguage = typeLanguage;
        this.bpmnprofile_rootelements = new ArrayList<>();
    }

    public BPMNProfile_Definitions(
        String exporter,        String exporterVersion,        String expressionLanguage,        String targetNamespace,        String typeLanguage        ArrayList<BPMNProfile_RootElement> bpmnprofile_rootelements    ) {
        this.exporter = exporter;
        this.exporterVersion = exporterVersion;
        this.expressionLanguage = expressionLanguage;
        this.targetNamespace = targetNamespace;
        this.typeLanguage = typeLanguage;
        this.bpmnprofile_rootelements = bpmnprofile_rootelements;
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

    public BPMNProfile_RootElement getBpmnprofile_rootelement() {
        return bpmnprofile_rootelement;
    }

    public void setBpmnprofile_rootelement(BPMNProfile_RootElement bpmnprofile_rootelement) {
        this.bpmnprofile_rootelement = bpmnprofile_rootelement;
    }
    public List<BPMNProfile_RootElement> getBpmnprofile_rootelements() {
        return bpmnprofile_rootelements;
    }

    public void addBpmnprofile_rootelement(Bpmnprofile_rootelement bpmnprofile_rootelement) {
        this.bpmnprofile_rootelements.add(bpmnprofile_rootelement);
    }

}