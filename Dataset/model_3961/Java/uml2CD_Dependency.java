





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Dependency extends DirectRelationship, PackageableElement {






    private uml2CD_NamedElement uml2cd_namedelement;




    private List<uml2CD_NamedElement> uml2cd_namedelements;




    private uml2CD_NamedElement uml2cd_namedelement;




    private List<uml2CD_NamedElement> uml2cd_namedelements;


    public uml2CD_Dependency(
    ) {
        super(
        );
        this.uml2cd_namedelements = new ArrayList<>();
        this.uml2cd_namedelements = new ArrayList<>();
    }

    public uml2CD_Dependency(
        ArrayList<uml2CD_NamedElement> uml2cd_namedelements,        ArrayList<uml2CD_NamedElement> uml2cd_namedelements    ) {
        this.uml2cd_namedelements = uml2cd_namedelements;
        this.uml2cd_namedelements = uml2cd_namedelements;
    }


    public uml2CD_NamedElement getUml2cd_namedelement() {
        return uml2cd_namedelement;
    }

    public void setUml2cd_namedelement(uml2CD_NamedElement uml2cd_namedelement) {
        this.uml2cd_namedelement = uml2cd_namedelement;
    }
    public List<uml2CD_NamedElement> getUml2cd_namedelements() {
        return uml2cd_namedelements;
    }

    public void addUml2cd_namedelement(Uml2cd_namedelement uml2cd_namedelement) {
        this.uml2cd_namedelements.add(uml2cd_namedelement);
    }
    public uml2CD_NamedElement getUml2cd_namedelement() {
        return uml2cd_namedelement;
    }

    public void setUml2cd_namedelement(uml2CD_NamedElement uml2cd_namedelement) {
        this.uml2cd_namedelement = uml2cd_namedelement;
    }
    public List<uml2CD_NamedElement> getUml2cd_namedelements() {
        return uml2cd_namedelements;
    }

    public void addUml2cd_namedelement(Uml2cd_namedelement uml2cd_namedelement) {
        this.uml2cd_namedelements.add(uml2cd_namedelement);
    }

}