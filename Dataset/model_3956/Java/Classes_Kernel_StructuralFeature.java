





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_StructuralFeature extends Kernel_Feature, Kernel_MultiplicityElement, Kernel_TypedElement {

    private boolean isReadOnly;



    public Classes_Kernel_StructuralFeature(
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