





import java.util.List;
import java.util.ArrayList;

public class spem_ToolDefinition extends MethodContentElement {






    private spem_TaskDefinition spem_taskdefinition;




    private List<spem_WorkProductDefinition> spem_workproductdefinitions;


    public spem_ToolDefinition(
    ) {
        super(
        );
        this.spem_workproductdefinitions = new ArrayList<>();
    }

    public spem_ToolDefinition(
        ArrayList<spem_WorkProductDefinition> spem_workproductdefinitions    ) {
        this.spem_workproductdefinitions = spem_workproductdefinitions;
    }


    public spem_TaskDefinition getSpem_taskdefinition() {
        return spem_taskdefinition;
    }

    public void setSpem_taskdefinition(spem_TaskDefinition spem_taskdefinition) {
        this.spem_taskdefinition = spem_taskdefinition;
    }
    public List<spem_WorkProductDefinition> getSpem_workproductdefinitions() {
        return spem_workproductdefinitions;
    }

    public void addSpem_workproductdefinition(Spem_workproductdefinition spem_workproductdefinition) {
        this.spem_workproductdefinitions.add(spem_workproductdefinition);
    }

}