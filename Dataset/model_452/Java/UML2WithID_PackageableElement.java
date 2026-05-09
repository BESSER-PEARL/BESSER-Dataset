





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_PackageableElement extends NamedElement, ParameterableElement {

    private String packageableElement_visibility;





    private UML2WithID_Component uml2withid_component;




    private UML2WithID_Namespace uml2withid_namespace;




    private UML2WithID_ElementImport uml2withid_elementimport;




    private UML2WithID_DeploymentTarget uml2withid_deploymenttarget;




    private UML2WithID_Manifestation uml2withid_manifestation;




    private UML2WithID_Package uml2withid_package;


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

    public UML2WithID_Component getUml2withid_component() {
        return uml2withid_component;
    }

    public void setUml2withid_component(UML2WithID_Component uml2withid_component) {
        this.uml2withid_component = uml2withid_component;
    }
    public UML2WithID_Namespace getUml2withid_namespace() {
        return uml2withid_namespace;
    }

    public void setUml2withid_namespace(UML2WithID_Namespace uml2withid_namespace) {
        this.uml2withid_namespace = uml2withid_namespace;
    }
    public UML2WithID_ElementImport getUml2withid_elementimport() {
        return uml2withid_elementimport;
    }

    public void setUml2withid_elementimport(UML2WithID_ElementImport uml2withid_elementimport) {
        this.uml2withid_elementimport = uml2withid_elementimport;
    }
    public UML2WithID_DeploymentTarget getUml2withid_deploymenttarget() {
        return uml2withid_deploymenttarget;
    }

    public void setUml2withid_deploymenttarget(UML2WithID_DeploymentTarget uml2withid_deploymenttarget) {
        this.uml2withid_deploymenttarget = uml2withid_deploymenttarget;
    }
    public UML2WithID_Manifestation getUml2withid_manifestation() {
        return uml2withid_manifestation;
    }

    public void setUml2withid_manifestation(UML2WithID_Manifestation uml2withid_manifestation) {
        this.uml2withid_manifestation = uml2withid_manifestation;
    }
    public UML2WithID_Package getUml2withid_package() {
        return uml2withid_package;
    }

    public void setUml2withid_package(UML2WithID_Package uml2withid_package) {
        this.uml2withid_package = uml2withid_package;
    }

}