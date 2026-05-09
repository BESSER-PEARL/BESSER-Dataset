





import java.util.List;
import java.util.ArrayList;

public class xmof_IntermediateActions_RemoveStructuralFeatureValueAction extends WriteStructuralFeatureAction {

    private boolean removeDuplicates;



    public xmof_IntermediateActions_RemoveStructuralFeatureValueAction(
        boolean removeDuplicates    ) {
        super(
        );
        this.removeDuplicates = removeDuplicates;
    }


    public boolean getRemoveduplicates() {
        return removeDuplicates;
    }

    public void setRemoveduplicates(boolean removeDuplicates) {
        this.removeDuplicates = removeDuplicates;
    }


}