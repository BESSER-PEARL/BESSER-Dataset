





import java.util.List;
import java.util.ArrayList;

public class assessment_Task extends Label, Notes {

    private String status;





    private assessment_Tasks assessment_tasks;




    private assessment_Tasks assessment_tasks;




    private assessment_Node assessment_node;




    private List<assessment_Node> assessment_nodes;


    public assessment_Task(
        String status    ) {
        super(
        );
        this.status = status;
        this.assessment_nodes = new ArrayList<>();
    }

    public assessment_Task(
        String status        ArrayList<assessment_Node> assessment_nodes    ) {
        this.status = status;
        this.assessment_nodes = assessment_nodes;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public assessment_Tasks getAssessment_tasks() {
        return assessment_tasks;
    }

    public void setAssessment_tasks(assessment_Tasks assessment_tasks) {
        this.assessment_tasks = assessment_tasks;
    }
    public assessment_Tasks getAssessment_tasks() {
        return assessment_tasks;
    }

    public void setAssessment_tasks(assessment_Tasks assessment_tasks) {
        this.assessment_tasks = assessment_tasks;
    }
    public assessment_Node getAssessment_node() {
        return assessment_node;
    }

    public void setAssessment_node(assessment_Node assessment_node) {
        this.assessment_node = assessment_node;
    }
    public List<assessment_Node> getAssessment_nodes() {
        return assessment_nodes;
    }

    public void addAssessment_node(Assessment_node assessment_node) {
        this.assessment_nodes.add(assessment_node);
    }

}