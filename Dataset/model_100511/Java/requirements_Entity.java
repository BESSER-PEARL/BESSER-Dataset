





import java.util.List;
import java.util.ArrayList;

public class requirements_Entity extends BasicElement {






    private requirements_Entity requirements_entity;




    private requirements_PrivilegeGroup requirements_privilegegroup;


    public requirements_Entity(
    ) {
        super(
        );
    }



    public requirements_Entity getRequirements_entity() {
        return requirements_entity;
    }

    public void setRequirements_entity(requirements_Entity requirements_entity) {
        this.requirements_entity = requirements_entity;
    }
    public requirements_PrivilegeGroup getRequirements_privilegegroup() {
        return requirements_privilegegroup;
    }

    public void setRequirements_privilegegroup(requirements_PrivilegeGroup requirements_privilegegroup) {
        this.requirements_privilegegroup = requirements_privilegegroup;
    }

}