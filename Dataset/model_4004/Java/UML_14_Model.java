





import java.util.List;
import java.util.ArrayList;

public class UML_14_Model  {






    private List<UML_14_Package> uml_14_packages;


    public UML_14_Model(
    ) {
        this.uml_14_packages = new ArrayList<>();
    }

    public UML_14_Model(
        ArrayList<UML_14_Package> uml_14_packages    ) {
        this.uml_14_packages = uml_14_packages;
    }


    public List<UML_14_Package> getUml_14_packages() {
        return uml_14_packages;
    }

    public void addUml_14_package(Uml_14_package uml_14_package) {
        this.uml_14_packages.add(uml_14_package);
    }

}