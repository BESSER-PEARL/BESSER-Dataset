





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Namespace extends NamedElement {






    private List<UML2WithID_NamedElement> uml2withid_namedelements;




    private List<UML2WithID_PackageableElement> uml2withid_packageableelements;


    public UML2WithID_Namespace(
    ) {
        super(
        );
        this.uml2withid_namedelements = new ArrayList<>();
        this.uml2withid_packageableelements = new ArrayList<>();
    }

    public UML2WithID_Namespace(
        ArrayList<UML2WithID_NamedElement> uml2withid_namedelements,        ArrayList<UML2WithID_PackageableElement> uml2withid_packageableelements    ) {
        this.uml2withid_namedelements = uml2withid_namedelements;
        this.uml2withid_packageableelements = uml2withid_packageableelements;
    }


    public List<UML2WithID_NamedElement> getUml2withid_namedelements() {
        return uml2withid_namedelements;
    }

    public void addUml2withid_namedelement(Uml2withid_namedelement uml2withid_namedelement) {
        this.uml2withid_namedelements.add(uml2withid_namedelement);
    }
    public List<UML2WithID_PackageableElement> getUml2withid_packageableelements() {
        return uml2withid_packageableelements;
    }

    public void addUml2withid_packageableelement(Uml2withid_packageableelement uml2withid_packageableelement) {
        this.uml2withid_packageableelements.add(uml2withid_packageableelement);
    }

}