





import java.util.List;
import java.util.ArrayList;

public class xmof_IntermediateActions_RemoveStructuralFeatureValueAction extends WriteStructuralFeatureAction {

    private boolean removeDuplicates;





    private BasicActions_InputPin basicactions_inputpin;


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

    public BasicActions_InputPin getBasicactions_inputpin() {
        return basicactions_inputpin;
    }

    public void setBasicactions_inputpin(BasicActions_InputPin basicactions_inputpin) {
        this.basicactions_inputpin = basicactions_inputpin;
    }

}