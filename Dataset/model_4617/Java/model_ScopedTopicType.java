





import java.util.List;
import java.util.ArrayList;

public class model_ScopedTopicType extends TopicType {






    private List<model_ScopeConstraint> model_scopeconstraints;


    public model_ScopedTopicType(
    ) {
        super(
        );
        this.model_scopeconstraints = new ArrayList<>();
    }

    public model_ScopedTopicType(
        ArrayList<model_ScopeConstraint> model_scopeconstraints    ) {
        this.model_scopeconstraints = model_scopeconstraints;
    }


    public List<model_ScopeConstraint> getModel_scopeconstraints() {
        return model_scopeconstraints;
    }

    public void addModel_scopeconstraint(Model_scopeconstraint model_scopeconstraint) {
        this.model_scopeconstraints.add(model_scopeconstraint);
    }

}