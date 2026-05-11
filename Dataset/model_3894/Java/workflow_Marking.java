





import java.util.List;
import java.util.ArrayList;

public class workflow_Marking extends State {






    private workflow_PetriNet workflow_petrinet;




    private List<workflow_Token> workflow_tokens;


    public workflow_Marking(
    ) {
        super(
        );
        this.workflow_tokens = new ArrayList<>();
    }

    public workflow_Marking(
        ArrayList<workflow_Token> workflow_tokens    ) {
        this.workflow_tokens = workflow_tokens;
    }


    public workflow_PetriNet getWorkflow_petrinet() {
        return workflow_petrinet;
    }

    public void setWorkflow_petrinet(workflow_PetriNet workflow_petrinet) {
        this.workflow_petrinet = workflow_petrinet;
    }
    public List<workflow_Token> getWorkflow_tokens() {
        return workflow_tokens;
    }

    public void addWorkflow_token(Workflow_token workflow_token) {
        this.workflow_tokens.add(workflow_token);
    }

}