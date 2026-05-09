





import java.util.List;
import java.util.ArrayList;

public class QVTBase_TypedModel extends NamedElement {






    private List<Package> packages;


    public QVTBase_TypedModel(
    ) {
        super(
        );
        this.packages = new ArrayList<>();
    }

    public QVTBase_TypedModel(
        ArrayList<Package> packages    ) {
        this.packages = packages;
    }


    public List<Package> getPackages() {
        return packages;
    }

    public void addPackage(Package package) {
        this.packages.add(package);
    }

}