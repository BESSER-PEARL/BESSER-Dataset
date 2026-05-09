





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_StructuralFeature extends MultiplicityElement, TypedElement, Feature {

    private String isReadOnly;





    private uml3_0_0_Slot uml3_0_0_slot;


    public uml3_0_0_StructuralFeature(
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

    public uml3_0_0_Slot getUml3_0_0_slot() {
        return uml3_0_0_slot;
    }

    public void setUml3_0_0_slot(uml3_0_0_Slot uml3_0_0_slot) {
        this.uml3_0_0_slot = uml3_0_0_slot;
    }

}