





import java.util.List;
import java.util.ArrayList;

public class model_AssociationType extends ScopedReifiableTopicType, ScopedTopicType {






    private List<model_RoleConstraint> model_roleconstraints;




    private List<model_RoleCombinationConstraint> model_rolecombinationconstraints;


    public model_AssociationType(
    ) {
        super(
        );
        this.model_roleconstraints = new ArrayList<>();
        this.model_rolecombinationconstraints = new ArrayList<>();
    }

    public model_AssociationType(
        ArrayList<model_RoleConstraint> model_roleconstraints,        ArrayList<model_RoleCombinationConstraint> model_rolecombinationconstraints    ) {
        this.model_roleconstraints = model_roleconstraints;
        this.model_rolecombinationconstraints = model_rolecombinationconstraints;
    }


    public List<model_RoleConstraint> getModel_roleconstraints() {
        return model_roleconstraints;
    }

    public void addModel_roleconstraint(Model_roleconstraint model_roleconstraint) {
        this.model_roleconstraints.add(model_roleconstraint);
    }
    public List<model_RoleCombinationConstraint> getModel_rolecombinationconstraints() {
        return model_rolecombinationconstraints;
    }

    public void addModel_rolecombinationconstraint(Model_rolecombinationconstraint model_rolecombinationconstraint) {
        this.model_rolecombinationconstraints.add(model_rolecombinationconstraint);
    }

}