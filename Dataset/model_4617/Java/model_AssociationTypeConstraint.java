





import java.util.List;
import java.util.ArrayList;

public class model_AssociationTypeConstraint extends AbstractTypedConstraint {






    private List<model_RolePlayerConstraint> model_roleplayerconstraints;




    private model_TopicMapSchema model_topicmapschema;


    public model_AssociationTypeConstraint(
    ) {
        super(
        );
        this.model_roleplayerconstraints = new ArrayList<>();
    }

    public model_AssociationTypeConstraint(
        ArrayList<model_RolePlayerConstraint> model_roleplayerconstraints    ) {
        this.model_roleplayerconstraints = model_roleplayerconstraints;
    }


    public List<model_RolePlayerConstraint> getModel_roleplayerconstraints() {
        return model_roleplayerconstraints;
    }

    public void addModel_roleplayerconstraint(Model_roleplayerconstraint model_roleplayerconstraint) {
        this.model_roleplayerconstraints.add(model_roleplayerconstraint);
    }
    public model_TopicMapSchema getModel_topicmapschema() {
        return model_topicmapschema;
    }

    public void setModel_topicmapschema(model_TopicMapSchema model_topicmapschema) {
        this.model_topicmapschema = model_topicmapschema;
    }

}