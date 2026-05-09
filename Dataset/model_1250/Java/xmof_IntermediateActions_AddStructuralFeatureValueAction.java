





import java.util.List;
import java.util.ArrayList;

public class xmof_IntermediateActions_AddStructuralFeatureValueAction extends WriteStructuralFeatureAction {

    private boolean replaceAll;



    public xmof_IntermediateActions_AddStructuralFeatureValueAction(
        boolean replaceAll    ) {
        super(
        );
        this.replaceAll = replaceAll;
    }


    public boolean getReplaceall() {
        return replaceAll;
    }

    public void setReplaceall(boolean replaceAll) {
        this.replaceAll = replaceAll;
    }


}