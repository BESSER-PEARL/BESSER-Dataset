





import java.util.List;
import java.util.ArrayList;

public class crom_l1_composed_Relationship extends Relation, NamedElement {

    private String direction;





    private List<crom_l1_composed_IntraRelationshipConstraint> crom_l1_composed_intrarelationshipconstraints;




    private crom_l1_composed_IntraRelationshipConstraint crom_l1_composed_intrarelationshipconstraint;




    private crom_l1_composed_CompartmentType crom_l1_composed_compartmenttype;


    public crom_l1_composed_Relationship(
        String direction    ) {
        super(
        );
        this.direction = direction;
        this.crom_l1_composed_intrarelationshipconstraints = new ArrayList<>();
    }

    public crom_l1_composed_Relationship(
        String direction        ArrayList<crom_l1_composed_IntraRelationshipConstraint> crom_l1_composed_intrarelationshipconstraints    ) {
        this.direction = direction;
        this.crom_l1_composed_intrarelationshipconstraints = crom_l1_composed_intrarelationshipconstraints;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public List<crom_l1_composed_IntraRelationshipConstraint> getCrom_l1_composed_intrarelationshipconstraints() {
        return crom_l1_composed_intrarelationshipconstraints;
    }

    public void addCrom_l1_composed_intrarelationshipconstraint(Crom_l1_composed_intrarelationshipconstraint crom_l1_composed_intrarelationshipconstraint) {
        this.crom_l1_composed_intrarelationshipconstraints.add(crom_l1_composed_intrarelationshipconstraint);
    }
    public crom_l1_composed_IntraRelationshipConstraint getCrom_l1_composed_intrarelationshipconstraint() {
        return crom_l1_composed_intrarelationshipconstraint;
    }

    public void setCrom_l1_composed_intrarelationshipconstraint(crom_l1_composed_IntraRelationshipConstraint crom_l1_composed_intrarelationshipconstraint) {
        this.crom_l1_composed_intrarelationshipconstraint = crom_l1_composed_intrarelationshipconstraint;
    }
    public crom_l1_composed_CompartmentType getCrom_l1_composed_compartmenttype() {
        return crom_l1_composed_compartmenttype;
    }

    public void setCrom_l1_composed_compartmenttype(crom_l1_composed_CompartmentType crom_l1_composed_compartmenttype) {
        this.crom_l1_composed_compartmenttype = crom_l1_composed_compartmenttype;
    }

}