





import java.util.List;
import java.util.ArrayList;

public class UML2_PackageableElement extends ParameterableElement, NamedElement {






    private UML2_ElementImport uml2_elementimport;


    public UML2_PackageableElement(
    ) {
        super(
        );
    }



    public UML2_ElementImport getUml2_elementimport() {
        return uml2_elementimport;
    }

    public void setUml2_elementimport(UML2_ElementImport uml2_elementimport) {
        this.uml2_elementimport = uml2_elementimport;
    }

}