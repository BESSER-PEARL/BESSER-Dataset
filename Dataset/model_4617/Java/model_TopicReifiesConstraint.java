





import java.util.List;
import java.util.ArrayList;

public class model_TopicReifiesConstraint extends AbstractTypedCardinalityConstraint {






    private model_TopicType model_topictype;


    public model_TopicReifiesConstraint(
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