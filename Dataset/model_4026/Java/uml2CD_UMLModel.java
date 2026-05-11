





import java.util.List;
import java.util.ArrayList;

public class uml2CD_UMLModel  {






    private List<uml2CD_Package> uml2cd_packages;


    public uml2CD_UMLModel(
    ) {
        this.uml2cd_packages = new ArrayList<>();
    }

    public uml2CD_UMLModel(
        ArrayList<uml2CD_Package> uml2cd_packages    ) {
        this.uml2cd_packages = uml2cd_packages;
    }


    public List<uml2CD_Package> getUml2cd_packages() {
        return uml2cd_packages;
    }

    public void addUml2cd_package(Uml2cd_package uml2cd_package) {
        this.uml2cd_packages.add(uml2cd_package);
    }

}