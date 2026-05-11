





import java.util.List;
import java.util.ArrayList;

public class carnot_TransitionType extends IIdentifiableModelElement {

    private String forkOnTraversal;
    private String condition;



    public carnot_TransitionType(
        String forkOnTraversal,        String condition    ) {
        super(
        );
        this.forkOnTraversal = forkOnTraversal;
        this.condition = condition;
    }


    public String getForkontraversal() {
        return forkOnTraversal;
    }

    public void setForkontraversal(String forkOnTraversal) {
        this.forkOnTraversal = forkOnTraversal;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }


}