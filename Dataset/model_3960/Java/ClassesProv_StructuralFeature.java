





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_StructuralFeature extends Feature, TypedElement, MultiplicityElement {

    private boolean isReadOnly;





    private ClassesProv_Slot classesprov_slot;


    public ClassesProv_StructuralFeature(
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

    public ClassesProv_Slot getClassesprov_slot() {
        return classesprov_slot;
    }

    public void setClassesprov_slot(ClassesProv_Slot classesprov_slot) {
        this.classesprov_slot = classesprov_slot;
    }

}