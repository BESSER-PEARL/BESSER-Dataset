





import java.util.List;
import java.util.ArrayList;

public class model_AbstractUniqueValueTopicType extends TopicType {

    private boolean unique;



    public model_AbstractUniqueValueTopicType(
        boolean unique    ) {
        super(
        );
        this.unique = unique;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }


}