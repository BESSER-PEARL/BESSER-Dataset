





import java.util.List;
import java.util.ArrayList;

public class model_SubjectLocatorConstraint extends AbstractRegExpConstraint, AbstractCardinalityConstraint {






    private model_TopicType model_topictype;


    public model_SubjectLocatorConstraint(
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

}