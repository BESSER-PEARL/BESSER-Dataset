





import java.util.List;
import java.util.ArrayList;

public class workflow_Workflow  {

    private String name;





    private List<workflow_Recipe> workflow_recipes;


    public workflow_Workflow(
        String name    ) {
        this.name = name;
        this.workflow_recipes = new ArrayList<>();
    }

    public workflow_Workflow(
        String name        ArrayList<workflow_Recipe> workflow_recipes    ) {
        this.name = name;
        this.workflow_recipes = workflow_recipes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<workflow_Recipe> getWorkflow_recipes() {
        return workflow_recipes;
    }

    public void addWorkflow_recipe(Workflow_recipe workflow_recipe) {
        this.workflow_recipes.add(workflow_recipe);
    }

}