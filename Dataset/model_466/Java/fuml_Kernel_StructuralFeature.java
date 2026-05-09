





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_StructuralFeature extends Kernel_Feature, Kernel_TypedElement, Kernel_MultiplicityElement {

    private boolean readOnly;



    public fuml_Kernel_StructuralFeature(
        boolean readOnly    ) {
        super(
        );
        this.readOnly = readOnly;
    }


    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }


}