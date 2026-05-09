





import java.util.List;
import java.util.ArrayList;

public class express_rules_Extent extends SETValue {






    private EntityType entitytype;




    private List<SubtypeConstraint> subtypeconstraints;


    public express_rules_Extent(
    ) {
        super(
        );
        this.subtypeconstraints = new ArrayList<>();
    }

    public express_rules_Extent(
        ArrayList<SubtypeConstraint> subtypeconstraints    ) {
        this.subtypeconstraints = subtypeconstraints;
    }


    public EntityType getEntitytype() {
        return entitytype;
    }

    public void setEntitytype(EntityType entitytype) {
        this.entitytype = entitytype;
    }
    public List<SubtypeConstraint> getSubtypeconstraints() {
        return subtypeconstraints;
    }

    public void addSubtypeconstraint(Subtypeconstraint subtypeconstraint) {
        this.subtypeconstraints.add(subtypeconstraint);
    }

}