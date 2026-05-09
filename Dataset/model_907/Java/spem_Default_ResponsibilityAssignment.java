





import java.util.List;
import java.util.ArrayList;

public class spem_Default_ResponsibilityAssignment extends MethodContentElement {






    private List<spem_RoleDefinition> spem_roledefinitions;




    private spem_WorkProductDefinition spem_workproductdefinition;


    public spem_Default_ResponsibilityAssignment(
    ) {
        super(
        );
        this.spem_roledefinitions = new ArrayList<>();
    }

    public spem_Default_ResponsibilityAssignment(
        ArrayList<spem_RoleDefinition> spem_roledefinitions    ) {
        this.spem_roledefinitions = spem_roledefinitions;
    }


    public List<spem_RoleDefinition> getSpem_roledefinitions() {
        return spem_roledefinitions;
    }

    public void addSpem_roledefinition(Spem_roledefinition spem_roledefinition) {
        this.spem_roledefinitions.add(spem_roledefinition);
    }
    public spem_WorkProductDefinition getSpem_workproductdefinition() {
        return spem_workproductdefinition;
    }

    public void setSpem_workproductdefinition(spem_WorkProductDefinition spem_workproductdefinition) {
        this.spem_workproductdefinition = spem_workproductdefinition;
    }

}