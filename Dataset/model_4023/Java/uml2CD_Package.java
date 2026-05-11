





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Package extends NamedElement {






    private List<uml2CD_Package> uml2cd_packages;




    private List<uml2CD_Generalization> uml2cd_generalizations;




    private List<uml2CD_PrimitiveType> uml2cd_primitivetypes;


    public uml2CD_Package(
    ) {
        super(
        );
        this.uml2cd_packages = new ArrayList<>();
        this.uml2cd_generalizations = new ArrayList<>();
        this.uml2cd_primitivetypes = new ArrayList<>();
    }

    public uml2CD_Package(
        ArrayList<uml2CD_Package> uml2cd_packages,        ArrayList<uml2CD_Generalization> uml2cd_generalizations,        ArrayList<uml2CD_PrimitiveType> uml2cd_primitivetypes    ) {
        this.uml2cd_packages = uml2cd_packages;
        this.uml2cd_generalizations = uml2cd_generalizations;
        this.uml2cd_primitivetypes = uml2cd_primitivetypes;
    }


    public List<uml2CD_Package> getUml2cd_packages() {
        return uml2cd_packages;
    }

    public void addUml2cd_package(Uml2cd_package uml2cd_package) {
        this.uml2cd_packages.add(uml2cd_package);
    }
    public List<uml2CD_Generalization> getUml2cd_generalizations() {
        return uml2cd_generalizations;
    }

    public void addUml2cd_generalization(Uml2cd_generalization uml2cd_generalization) {
        this.uml2cd_generalizations.add(uml2cd_generalization);
    }
    public List<uml2CD_PrimitiveType> getUml2cd_primitivetypes() {
        return uml2cd_primitivetypes;
    }

    public void addUml2cd_primitivetype(Uml2cd_primitivetype uml2cd_primitivetype) {
        this.uml2cd_primitivetypes.add(uml2cd_primitivetype);
    }

}