





import java.util.List;
import java.util.ArrayList;

public class cmof_StructuralFeature extends MultiplicityElement, Feature, TypedElement {

    private String isReadOnly;



    public cmof_StructuralFeature(
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