





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_StructuralFeature extends Feature, MultiplicityElement, TypedElement {

    private boolean isReadOnly;





    private UML2WithID_Slot uml2withid_slot;


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

    public UML2WithID_Slot getUml2withid_slot() {
        return uml2withid_slot;
    }

    public void setUml2withid_slot(UML2WithID_Slot uml2withid_slot) {
        this.uml2withid_slot = uml2withid_slot;
    }

}