





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_StructuralFeature extends Feature, MultiplicityElement, TypedElement {

    private boolean isReadOnly;



    public UML2WithID_StructuralFeature(
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