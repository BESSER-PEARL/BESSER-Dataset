





import java.util.List;
import java.util.ArrayList;

public class assessment_Finding extends Label, Notes {

    private String remediation;
    private String reproducer;
    private String references;





    private assessment_Node assessment_node;




    private assessment_Findings assessment_findings;




    private assessment_Findings assessment_findings;




    private List<assessment_Node> assessment_nodes;


    public assessment_Finding(
        String remediation,        String reproducer,        String references    ) {
        super(
        );
        this.remediation = remediation;
        this.reproducer = reproducer;
        this.references = references;
        this.assessment_nodes = new ArrayList<>();
    }

    public assessment_Finding(
        String remediation,        String reproducer,        String references        ArrayList<assessment_Node> assessment_nodes    ) {
        this.remediation = remediation;
        this.reproducer = reproducer;
        this.references = references;
        this.assessment_nodes = assessment_nodes;
    }

    public String getRemediation() {
        return remediation;
    }

    public void setRemediation(String remediation) {
        this.remediation = remediation;
    }
    public String getReproducer() {
        return reproducer;
    }

    public void setReproducer(String reproducer) {
        this.reproducer = reproducer;
    }
    public String getReferences() {
        return references;
    }

    public void setReferences(String references) {
        this.references = references;
    }

    public assessment_Node getAssessment_node() {
        return assessment_node;
    }

    public void setAssessment_node(assessment_Node assessment_node) {
        this.assessment_node = assessment_node;
    }
    public assessment_Findings getAssessment_findings() {
        return assessment_findings;
    }

    public void setAssessment_findings(assessment_Findings assessment_findings) {
        this.assessment_findings = assessment_findings;
    }
    public assessment_Findings getAssessment_findings() {
        return assessment_findings;
    }

    public void setAssessment_findings(assessment_Findings assessment_findings) {
        this.assessment_findings = assessment_findings;
    }
    public List<assessment_Node> getAssessment_nodes() {
        return assessment_nodes;
    }

    public void addAssessment_node(Assessment_node assessment_node) {
        this.assessment_nodes.add(assessment_node);
    }

}