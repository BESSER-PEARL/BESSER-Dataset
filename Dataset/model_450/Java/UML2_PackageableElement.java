





import java.util.List;
import java.util.ArrayList;

public class UML2_PackageableElement extends NamedElement, ParameterableElement {

    private String packageableElement_visibility;





    private UML2_Package uml2_package;




    private UML2_Component uml2_component;




    private UML2_Manifestation uml2_manifestation;




    private UML2_Namespace uml2_namespace;




    private UML2_ElementImport uml2_elementimport;


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

    public UML2_Package getUml2_package() {
        return uml2_package;
    }

    public void setUml2_package(UML2_Package uml2_package) {
        this.uml2_package = uml2_package;
    }
    public UML2_Component getUml2_component() {
        return uml2_component;
    }

    public void setUml2_component(UML2_Component uml2_component) {
        this.uml2_component = uml2_component;
    }
    public UML2_Manifestation getUml2_manifestation() {
        return uml2_manifestation;
    }

    public void setUml2_manifestation(UML2_Manifestation uml2_manifestation) {
        this.uml2_manifestation = uml2_manifestation;
    }
    public UML2_Namespace getUml2_namespace() {
        return uml2_namespace;
    }

    public void setUml2_namespace(UML2_Namespace uml2_namespace) {
        this.uml2_namespace = uml2_namespace;
    }
    public UML2_ElementImport getUml2_elementimport() {
        return uml2_elementimport;
    }

    public void setUml2_elementimport(UML2_ElementImport uml2_elementimport) {
        this.uml2_elementimport = uml2_elementimport;
    }

}