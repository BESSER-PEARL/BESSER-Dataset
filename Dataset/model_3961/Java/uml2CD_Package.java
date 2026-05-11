





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Package extends Namespace, PackageableElement {






    private uml2CD_Package uml2cd_package;




    private uml2CD_Package uml2cd_package;




    private List<uml2CD_PackageableElement> uml2cd_packageableelements;




    private uml2CD_PackageableElement uml2cd_packageableelement;


    public uml2CD_Package(
    ) {
        super(
        );
        this.uml2cd_packageableelements = new ArrayList<>();
    }

    public uml2CD_Package(
        ArrayList<uml2CD_PackageableElement> uml2cd_packageableelements    ) {
        this.uml2cd_packageableelements = uml2cd_packageableelements;
    }


    public uml2CD_Package getUml2cd_package() {
        return uml2cd_package;
    }

    public void setUml2cd_package(uml2CD_Package uml2cd_package) {
        this.uml2cd_package = uml2cd_package;
    }
    public uml2CD_Package getUml2cd_package() {
        return uml2cd_package;
    }

    public void setUml2cd_package(uml2CD_Package uml2cd_package) {
        this.uml2cd_package = uml2cd_package;
    }
    public List<uml2CD_PackageableElement> getUml2cd_packageableelements() {
        return uml2cd_packageableelements;
    }

    public void addUml2cd_packageableelement(Uml2cd_packageableelement uml2cd_packageableelement) {
        this.uml2cd_packageableelements.add(uml2cd_packageableelement);
    }
    public uml2CD_PackageableElement getUml2cd_packageableelement() {
        return uml2cd_packageableelement;
    }

    public void setUml2cd_packageableelement(uml2CD_PackageableElement uml2cd_packageableelement) {
        this.uml2cd_packageableelement = uml2cd_packageableelement;
    }

}