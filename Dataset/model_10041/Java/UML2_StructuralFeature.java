





import java.util.List;
import java.util.ArrayList;

public class UML2_StructuralFeature extends MultiplicityElement, Feature, TypedElement {

    private boolean isReadOnly;





    private UML2_Slot uml2_slot;


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

    public UML2_Slot getUml2_slot() {
        return uml2_slot;
    }

    public void setUml2_slot(UML2_Slot uml2_slot) {
        this.uml2_slot = uml2_slot;
    }

}