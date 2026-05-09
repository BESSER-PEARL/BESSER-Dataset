





import java.util.List;
import java.util.ArrayList;

public class UML2_AddStructuralFeatureValueAction extends WriteStructuralFeatureAction {

    private boolean isReplaceAll;





    private UML2_InputPin uml2_inputpin;


    public UML2_AddStructuralFeatureValueAction(
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

    public UML2_InputPin getUml2_inputpin() {
        return uml2_inputpin;
    }

    public void setUml2_inputpin(UML2_InputPin uml2_inputpin) {
        this.uml2_inputpin = uml2_inputpin;
    }

}