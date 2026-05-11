





import java.util.List;
import java.util.ArrayList;

public class workflow_DocumentTypeContainer extends GlobalAspect {

    private String name;





    private List<workflow_DocumentType> workflow_documenttypes;


    public workflow_DocumentTypeContainer(
        String name    ) {
        super(
        );
        this.name = name;
        this.workflow_documenttypes = new ArrayList<>();
    }

    public workflow_DocumentTypeContainer(
        String name        ArrayList<workflow_DocumentType> workflow_documenttypes    ) {
        this.name = name;
        this.workflow_documenttypes = workflow_documenttypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<workflow_DocumentType> getWorkflow_documenttypes() {
        return workflow_documenttypes;
    }

    public void addWorkflow_documenttype(Workflow_documenttype workflow_documenttype) {
        this.workflow_documenttypes.add(workflow_documenttype);
    }

}