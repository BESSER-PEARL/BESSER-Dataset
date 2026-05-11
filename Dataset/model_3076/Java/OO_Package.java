





import java.util.List;
import java.util.ArrayList;

public class OO_Package extends PackageableElement {






    private List<OO_Package> oo_packages;


    public OO_Package(
    ) {
        super(
        );
        this.oo_packages = new ArrayList<>();
    }

    public OO_Package(
        ArrayList<OO_Package> oo_packages    ) {
        this.oo_packages = oo_packages;
    }


    public List<OO_Package> getOo_packages() {
        return oo_packages;
    }

    public void addOo_package(Oo_package oo_package) {
        this.oo_packages.add(oo_package);
    }

}