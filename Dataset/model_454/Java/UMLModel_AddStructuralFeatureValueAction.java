





import java.util.List;
import java.util.ArrayList;

public class UMLModel_AddStructuralFeatureValueAction extends WriteStructuralFeatureAction {

    private String isReplaceAll;



    public UMLModel_AddStructuralFeatureValueAction(
        String isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
    }


    public String getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(String isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }


}