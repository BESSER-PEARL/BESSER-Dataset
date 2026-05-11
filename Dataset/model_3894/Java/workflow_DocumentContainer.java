





import java.util.List;
import java.util.ArrayList;

public class workflow_DocumentContainer extends RuntimeGlobalAspect {

    private String name;





    private List<workflow_Document> workflow_documents;


    public workflow_DocumentContainer(
        String name    ) {
        super(
        );
        this.name = name;
        this.workflow_documents = new ArrayList<>();
    }

    public workflow_DocumentContainer(
        String name        ArrayList<workflow_Document> workflow_documents    ) {
        this.name = name;
        this.workflow_documents = workflow_documents;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<workflow_Document> getWorkflow_documents() {
        return workflow_documents;
    }

    public void addWorkflow_document(Workflow_document workflow_document) {
        this.workflow_documents.add(workflow_document);
    }

}