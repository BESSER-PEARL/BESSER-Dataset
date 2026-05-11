





import java.util.List;
import java.util.ArrayList;

public class Activities_IntermediateActivities_JoinNode extends ControlNode {

    private boolean isCombineDuplicate;





    private ValueSpecification valuespecification;


    public Activities_IntermediateActivities_JoinNode(
        boolean isCombineDuplicate    ) {
        super(
        );
        this.isCombineDuplicate = isCombineDuplicate;
    }


    public boolean getIscombineduplicate() {
        return isCombineDuplicate;
    }

    public void setIscombineduplicate(boolean isCombineDuplicate) {
        this.isCombineDuplicate = isCombineDuplicate;
    }

    public ValueSpecification getValuespecification() {
        return valuespecification;
    }

    public void setValuespecification(ValueSpecification valuespecification) {
        this.valuespecification = valuespecification;
    }

}