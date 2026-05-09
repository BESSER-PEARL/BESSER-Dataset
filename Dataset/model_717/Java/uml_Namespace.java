





import java.util.List;
import java.util.ArrayList;

public class uml_Namespace extends NamedElement {






    private List<uml_NamedElement> uml_namedelements;




    private uml_NamedElement uml_namedelement;




    private List<uml_NamedElement> uml_namedelements;




    private List<uml_PackageableElement> uml_packageableelements;


    public uml_Namespace(
    ) {
        super(
        );
        this.uml_namedelements = new ArrayList<>();
        this.uml_namedelements = new ArrayList<>();
        this.uml_packageableelements = new ArrayList<>();
    }

    public uml_Namespace(
        ArrayList<uml_NamedElement> uml_namedelements,        ArrayList<uml_NamedElement> uml_namedelements,        ArrayList<uml_PackageableElement> uml_packageableelements    ) {
        this.uml_namedelements = uml_namedelements;
        this.uml_namedelements = uml_namedelements;
        this.uml_packageableelements = uml_packageableelements;
    }


    public List<uml_NamedElement> getUml_namedelements() {
        return uml_namedelements;
    }

    public void addUml_namedelement(Uml_namedelement uml_namedelement) {
        this.uml_namedelements.add(uml_namedelement);
    }
    public uml_NamedElement getUml_namedelement() {
        return uml_namedelement;
    }

    public void setUml_namedelement(uml_NamedElement uml_namedelement) {
        this.uml_namedelement = uml_namedelement;
    }
    public List<uml_NamedElement> getUml_namedelements() {
        return uml_namedelements;
    }

    public void addUml_namedelement(Uml_namedelement uml_namedelement) {
        this.uml_namedelements.add(uml_namedelement);
    }
    public List<uml_PackageableElement> getUml_packageableelements() {
        return uml_packageableelements;
    }

    public void addUml_packageableelement(Uml_packageableelement uml_packageableelement) {
        this.uml_packageableelements.add(uml_packageableelement);
    }

}