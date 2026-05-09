





import java.util.List;
import java.util.ArrayList;

public class UMLModel_RemoveStructuralFeatureValueAction extends WriteStructuralFeatureAction {

    private String isRemoveDuplicates;



    public UMLModel_RemoveStructuralFeatureValueAction(
        String isRemoveDuplicates    ) {
        super(
        );
        this.isRemoveDuplicates = isRemoveDuplicates;
    }


    public String getIsremoveduplicates() {
        return isRemoveDuplicates;
    }

    public void setIsremoveduplicates(String isRemoveDuplicates) {
        this.isRemoveDuplicates = isRemoveDuplicates;
    }


}