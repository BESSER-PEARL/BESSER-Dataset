





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_AddVariableValueAction extends WriteVariableAction {

    private boolean isReplaceAll;



    public UML2WithID_AddVariableValueAction(
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