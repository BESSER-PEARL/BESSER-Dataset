





import java.util.List;
import java.util.ArrayList;

public class UMLModel_StructuralFeature extends TypedElement, Feature, MultiplicityElement {

    private String isReadOnly;



    public UMLModel_StructuralFeature(
        String isReadOnly    ) {
        super(
        );
        this.isReadOnly = isReadOnly;
    }


    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }


}