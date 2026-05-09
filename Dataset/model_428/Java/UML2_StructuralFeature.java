





import java.util.List;
import java.util.ArrayList;

public class UML2_StructuralFeature extends MultiplicityElement, TypedElement, Feature {

    private boolean isReadOnly;





    private UML2_StructuralFeatureAction uml2_structuralfeatureaction;


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

    public UML2_StructuralFeatureAction getUml2_structuralfeatureaction() {
        return uml2_structuralfeatureaction;
    }

    public void setUml2_structuralfeatureaction(UML2_StructuralFeatureAction uml2_structuralfeatureaction) {
        this.uml2_structuralfeatureaction = uml2_structuralfeatureaction;
    }

}