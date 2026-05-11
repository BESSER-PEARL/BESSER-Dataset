





import java.util.List;
import java.util.ArrayList;

public class ActionsProv_ReclassifyObjectAction extends Action {

    private boolean isReplaceAll;



    public ActionsProv_ReclassifyObjectAction(
        boolean isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
    }


    public boolean getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(boolean isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }


}