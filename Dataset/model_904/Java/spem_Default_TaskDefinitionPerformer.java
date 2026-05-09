





import java.util.List;
import java.util.ArrayList;

public class spem_Default_TaskDefinitionPerformer extends MethodContentElement {






    private spem_TaskDefinition spem_taskdefinition;




    private List<spem_RoleDefinition> spem_roledefinitions;


    public spem_Default_TaskDefinitionPerformer(
    ) {
        super(
        );
        this.spem_roledefinitions = new ArrayList<>();
    }

    public spem_Default_TaskDefinitionPerformer(
        ArrayList<spem_RoleDefinition> spem_roledefinitions    ) {
        this.spem_roledefinitions = spem_roledefinitions;
    }


    public spem_TaskDefinition getSpem_taskdefinition() {
        return spem_taskdefinition;
    }

    public void setSpem_taskdefinition(spem_TaskDefinition spem_taskdefinition) {
        this.spem_taskdefinition = spem_taskdefinition;
    }
    public List<spem_RoleDefinition> getSpem_roledefinitions() {
        return spem_roledefinitions;
    }

    public void addSpem_roledefinition(Spem_roledefinition spem_roledefinition) {
        this.spem_roledefinitions.add(spem_roledefinition);
    }

}