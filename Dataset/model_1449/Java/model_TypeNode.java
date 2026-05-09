





import java.util.List;
import java.util.ArrayList;

public class model_TypeNode extends Node {

    private String topicType;



    public model_TypeNode(
        String topicType    ) {
        super(
        );
        this.topicType = topicType;
    }


    public String getTopictype() {
        return topicType;
    }

    public void setTopictype(String topicType) {
        this.topicType = topicType;
    }


}