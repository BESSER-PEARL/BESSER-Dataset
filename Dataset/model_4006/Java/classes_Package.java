





import java.util.List;
import java.util.ArrayList;

public class classes_Package extends NamedElement, Namespace {






    private classes_Root classes_root;




    private List<classes_Package> classes_packages;


    public classes_Package(
    ) {
        super(
        );
        this.classes_packages = new ArrayList<>();
    }

    public classes_Package(
        ArrayList<classes_Package> classes_packages    ) {
        this.classes_packages = classes_packages;
    }


    public classes_Root getClasses_root() {
        return classes_root;
    }

    public void setClasses_root(classes_Root classes_root) {
        this.classes_root = classes_root;
    }
    public List<classes_Package> getClasses_packages() {
        return classes_packages;
    }

    public void addClasses_package(Classes_package classes_package) {
        this.classes_packages.add(classes_package);
    }

}