





import java.util.List;
import java.util.ArrayList;

public class types_Package extends DomainElement, Declaration {






    private List<types_Package> types_packages;


    public types_Package(
    ) {
        super(
        );
        this.types_packages = new ArrayList<>();
    }

    public types_Package(
        ArrayList<types_Package> types_packages    ) {
        this.types_packages = types_packages;
    }


    public List<types_Package> getTypes_packages() {
        return types_packages;
    }

    public void addTypes_package(Types_package types_package) {
        this.types_packages.add(types_package);
    }

}