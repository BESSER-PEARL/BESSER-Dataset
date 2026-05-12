





import java.util.List;
import java.util.ArrayList;

public class requirements_Entity extends BasicElement {






    private requirements_PrivilegeGroup requirements_privilegegroup;




    private requirements_RelationShip requirements_relationship;




    private requirements_Entity requirements_entity;




    private requirements_RelationShip requirements_relationship;




    private List<requirements_Attribute> requirements_attributes;


    public requirements_Entity(
    ) {
        super(
        );
        this.requirements_attributes = new ArrayList<>();
    }

    public requirements_Entity(
        ArrayList<requirements_Attribute> requirements_attributes    ) {
        this.requirements_attributes = requirements_attributes;
    }


    public requirements_PrivilegeGroup getRequirements_privilegegroup() {
        return requirements_privilegegroup;
    }

    public void setRequirements_privilegegroup(requirements_PrivilegeGroup requirements_privilegegroup) {
        this.requirements_privilegegroup = requirements_privilegegroup;
    }
    public requirements_RelationShip getRequirements_relationship() {
        return requirements_relationship;
    }

    public void setRequirements_relationship(requirements_RelationShip requirements_relationship) {
        this.requirements_relationship = requirements_relationship;
    }
    public requirements_Entity getRequirements_entity() {
        return requirements_entity;
    }

    public void setRequirements_entity(requirements_Entity requirements_entity) {
        this.requirements_entity = requirements_entity;
    }
    public requirements_RelationShip getRequirements_relationship() {
        return requirements_relationship;
    }

    public void setRequirements_relationship(requirements_RelationShip requirements_relationship) {
        this.requirements_relationship = requirements_relationship;
    }
    public List<requirements_Attribute> getRequirements_attributes() {
        return requirements_attributes;
    }

    public void addRequirements_attribute(Requirements_attribute requirements_attribute) {
        this.requirements_attributes.add(requirements_attribute);
    }

}