





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_StructuralFeature extends TypedElement, MultiplicityElement, Feature {

    private String isReadOnly;





    private RefOntoUML_Slot refontouml_slot;


    public RefOntoUML_StructuralFeature(
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

    public RefOntoUML_Slot getRefontouml_slot() {
        return refontouml_slot;
    }

    public void setRefontouml_slot(RefOntoUML_Slot refontouml_slot) {
        this.refontouml_slot = refontouml_slot;
    }

}