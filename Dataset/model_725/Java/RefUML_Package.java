





import java.util.List;
import java.util.ArrayList;

public class RefUML_Package extends Namespace, PackageableElement {






    private List<RefUML_Package> refuml_packages;




    private RefUML_Package refuml_package;


    public RefUML_Package(
    ) {
        super(
        );
        this.refuml_packages = new ArrayList<>();
    }

    public RefUML_Package(
        ArrayList<RefUML_Package> refuml_packages    ) {
        this.refuml_packages = refuml_packages;
    }


    public List<RefUML_Package> getRefuml_packages() {
        return refuml_packages;
    }

    public void addRefuml_package(Refuml_package refuml_package) {
        this.refuml_packages.add(refuml_package);
    }
    public RefUML_Package getRefuml_package() {
        return refuml_package;
    }

    public void setRefuml_package(RefUML_Package refuml_package) {
        this.refuml_package = refuml_package;
    }

}