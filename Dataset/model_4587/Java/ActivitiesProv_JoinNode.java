





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_JoinNode extends ControlNode {

    private boolean isCombineDuplicate;



    public ActivitiesProv_JoinNode(
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


}