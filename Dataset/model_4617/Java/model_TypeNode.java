





import java.util.List;
import java.util.ArrayList;

public class model_TypeNode extends Node {

    private String image;





    private model_TopicType model_topictype;


    public model_TypeNode(
        String image    ) {
        super(
        );
        this.image = image;
    }


    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public model_TopicType getModel_topictype() {
        return model_topictype;
    }

    public void setModel_topictype(model_TopicType model_topictype) {
        this.model_topictype = model_topictype;
    }

}