





import java.util.List;
import java.util.ArrayList;

public class UML2_PackageableElement extends ParameterableElement, NamedElement {

    private String packageableElement_visibility;





    private UML2_Namespace uml2_namespace;


    public UML2_PackageableElement(
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

    public UML2_Namespace getUml2_namespace() {
        return uml2_namespace;
    }

    public void setUml2_namespace(UML2_Namespace uml2_namespace) {
        this.uml2_namespace = uml2_namespace;
    }

}