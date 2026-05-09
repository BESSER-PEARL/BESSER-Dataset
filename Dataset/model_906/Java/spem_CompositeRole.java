





import java.util.List;
import java.util.ArrayList;

public class spem_CompositeRole extends RoleUse {






    private List<spem_RoleDefinition> spem_roledefinitions;


    public spem_CompositeRole(
    ) {
        super(
        );
        this.spem_roledefinitions = new ArrayList<>();
    }

    public spem_CompositeRole(
        ArrayList<spem_RoleDefinition> spem_roledefinitions    ) {
        this.spem_roledefinitions = spem_roledefinitions;
    }


    public List<spem_RoleDefinition> getSpem_roledefinitions() {
        return spem_roledefinitions;
    }

    public void addSpem_roledefinition(Spem_roledefinition spem_roledefinition) {
        this.spem_roledefinitions.add(spem_roledefinition);
    }

}