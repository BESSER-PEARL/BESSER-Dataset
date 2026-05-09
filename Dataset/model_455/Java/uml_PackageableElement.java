





import java.util.List;
import java.util.ArrayList;

public class uml_PackageableElement extends NamedElement, ParameterableElement {






    private uml_ElementImport uml_elementimport;




    private uml_Package uml_package;


    public uml_PackageableElement(
    ) {
        super(
        );
    }



    public uml_ElementImport getUml_elementimport() {
        return uml_elementimport;
    }

    public void setUml_elementimport(uml_ElementImport uml_elementimport) {
        this.uml_elementimport = uml_elementimport;
    }
    public uml_Package getUml_package() {
        return uml_package;
    }

    public void setUml_package(uml_Package uml_package) {
        this.uml_package = uml_package;
    }

}