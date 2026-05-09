





import java.util.List;
import java.util.ArrayList;

public class UML2_StructuralFeature extends MultiplicityElement, Feature, TypedElement {

    private boolean isReadOnly;



    public UML2_StructuralFeature(
        boolean isReadOnly    ) {
        super(
        );
        this.isReadOnly = isReadOnly;
    }


    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
    }


}