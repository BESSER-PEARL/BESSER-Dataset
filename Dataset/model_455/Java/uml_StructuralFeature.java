





import java.util.List;
import java.util.ArrayList;

public class uml_StructuralFeature extends Feature, MultiplicityElement, TypedElement {

    private String isReadOnly;





    private uml_Slot uml_slot;


    public uml_StructuralFeature(
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

    public uml_Slot getUml_slot() {
        return uml_slot;
    }

    public void setUml_slot(uml_Slot uml_slot) {
        this.uml_slot = uml_slot;
    }

}