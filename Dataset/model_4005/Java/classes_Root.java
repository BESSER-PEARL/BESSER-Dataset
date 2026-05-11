





import java.util.List;
import java.util.ArrayList;

public class classes_Root  {






    private List<classes_Package> classes_packages;


    public classes_Root(
    ) {
        this.classes_packages = new ArrayList<>();
    }

    public classes_Root(
        ArrayList<classes_Package> classes_packages    ) {
        this.classes_packages = classes_packages;
    }


    public List<classes_Package> getClasses_packages() {
        return classes_packages;
    }

    public void addClasses_package(Classes_package classes_package) {
        this.classes_packages.add(classes_package);
    }

}