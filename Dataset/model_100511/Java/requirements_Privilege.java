





import java.util.List;
import java.util.ArrayList;

public class requirements_Privilege  {

    private String category;





    private requirements_BasicElement requirements_basicelement;




    private requirements_PrivilegeGroup requirements_privilegegroup;


    public requirements_Privilege(
        String category    ) {
        this.category = category;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public requirements_BasicElement getRequirements_basicelement() {
        return requirements_basicelement;
    }

    public void setRequirements_basicelement(requirements_BasicElement requirements_basicelement) {
        this.requirements_basicelement = requirements_basicelement;
    }
    public requirements_PrivilegeGroup getRequirements_privilegegroup() {
        return requirements_privilegegroup;
    }

    public void setRequirements_privilegegroup(requirements_PrivilegeGroup requirements_privilegegroup) {
        this.requirements_privilegegroup = requirements_privilegegroup;
    }

}