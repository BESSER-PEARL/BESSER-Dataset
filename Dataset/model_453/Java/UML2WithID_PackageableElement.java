





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_PackageableElement extends ParameterableElement, NamedElement {

    private String packageableElement_visibility;



    public UML2WithID_PackageableElement(
        String packageableElement_visibility    ) {
        super(
        );
        this.packageableElement_visibility = packageableElement_visibility;
    }


    public String getPackageableelement_visibility() {
        return packageableElement_visibility;
    }

    public void setPackageableelement_visibility(String packageableElement_visibility) {
        this.packageableElement_visibility = packageableElement_visibility;
    }


}