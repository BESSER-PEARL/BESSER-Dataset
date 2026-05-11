





import java.util.List;
import java.util.ArrayList;

public class classes_StructuralFeature extends TypedElement, Feature, MultiplicityElement {

    private boolean readOnly;



    public classes_StructuralFeature(
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