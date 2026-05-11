





import java.util.List;
import java.util.ArrayList;

public class model_RolePlayerConstraint extends AbstractCardinalityConstraint {






    private model_TopicType model_topictype;




    private model_RoleConstraint model_roleconstraint;


    public model_RolePlayerConstraint(
    ) {
        super(
        );
    }



    public model_TopicType getModel_topictype() {
        return model_topictype;
    }

    public void setModel_topictype(model_TopicType model_topictype) {
        this.model_topictype = model_topictype;
    }
    public model_RoleConstraint getModel_roleconstraint() {
        return model_roleconstraint;
    }

    public void setModel_roleconstraint(model_RoleConstraint model_roleconstraint) {
        this.model_roleconstraint = model_roleconstraint;
    }

}