





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Definitions extends BaseElement {

    private String exporterVersion;
    private String targetNamespace;
    private String typeLanguage;
    private String expressionLanguage;
    private String exporter;





    private List<BPMNProfile_BPMNRelationship> bpmnprofile_bpmnrelationships;




    private BPMNProfile_BPMNRelationship bpmnprofile_bpmnrelationship;




    private BPMNProfile_RootElement bpmnprofile_rootelement;




    private List<BPMNProfile_RootElement> bpmnprofile_rootelements;


    public BPMNProfile_Definitions(
        String exporterVersion,        String targetNamespace,        String typeLanguage,        String expressionLanguage,        String exporter    ) {
        super(
        );
        this.exporterVersion = exporterVersion;
        this.targetNamespace = targetNamespace;
        this.typeLanguage = typeLanguage;
        this.expressionLanguage = expressionLanguage;
        this.exporter = exporter;
        this.bpmnprofile_bpmnrelationships = new ArrayList<>();
        this.bpmnprofile_rootelements = new ArrayList<>();
    }

    public BPMNProfile_Definitions(
        String exporterVersion,        String targetNamespace,        String typeLanguage,        String expressionLanguage,        String exporter        ArrayList<BPMNProfile_BPMNRelationship> bpmnprofile_bpmnrelationships,        ArrayList<BPMNProfile_RootElement> bpmnprofile_rootelements    ) {
        this.exporterVersion = exporterVersion;
        this.targetNamespace = targetNamespace;
        this.typeLanguage = typeLanguage;
        this.expressionLanguage = expressionLanguage;
        this.exporter = exporter;
        this.bpmnprofile_bpmnrelationships = bpmnprofile_bpmnrelationships;
        this.bpmnprofile_rootelements = bpmnprofile_rootelements;
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
    public String getExporter() {
        return exporter;
    }

    public void setExporter(String exporter) {
        this.exporter = exporter;
    }

    public List<BPMNProfile_BPMNRelationship> getBpmnprofile_bpmnrelationships() {
        return bpmnprofile_bpmnrelationships;
    }

    public void addBpmnprofile_bpmnrelationship(Bpmnprofile_bpmnrelationship bpmnprofile_bpmnrelationship) {
        this.bpmnprofile_bpmnrelationships.add(bpmnprofile_bpmnrelationship);
    }
    public BPMNProfile_BPMNRelationship getBpmnprofile_bpmnrelationship() {
        return bpmnprofile_bpmnrelationship;
    }

    public void setBpmnprofile_bpmnrelationship(BPMNProfile_BPMNRelationship bpmnprofile_bpmnrelationship) {
        this.bpmnprofile_bpmnrelationship = bpmnprofile_bpmnrelationship;
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