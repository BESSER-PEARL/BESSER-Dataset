





import java.util.List;
import java.util.ArrayList;

public class RefUML_StructuralFeature extends Feature, MultiplicityElement, TypedElement {

    private String isReadOnly;



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


}