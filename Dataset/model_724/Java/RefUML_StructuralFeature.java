





import java.util.List;
import java.util.ArrayList;

public class RefUML_StructuralFeature extends MultiplicityElement, Feature, TypedElement {

    private String isReadOnly;





    private RefUML_Slot refuml_slot;


    public RefUML_StructuralFeature(
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

    public RefUML_Slot getRefuml_slot() {
        return refuml_slot;
    }

    public void setRefuml_slot(RefUML_Slot refuml_slot) {
        this.refuml_slot = refuml_slot;
    }

}