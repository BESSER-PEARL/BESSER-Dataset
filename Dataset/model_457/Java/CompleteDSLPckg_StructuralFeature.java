





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_StructuralFeature extends TypedElement, Feature, MultiplicityElement {

    private boolean isReadOnly;





    private CompleteDSLPckg_Slot completedslpckg_slot;


    public CompleteDSLPckg_StructuralFeature(
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

    public CompleteDSLPckg_Slot getCompletedslpckg_slot() {
        return completedslpckg_slot;
    }

    public void setCompletedslpckg_slot(CompleteDSLPckg_Slot completedslpckg_slot) {
        this.completedslpckg_slot = completedslpckg_slot;
    }

}