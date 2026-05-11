





import java.util.List;
import java.util.ArrayList;

public class soopl_Package extends NamedElement {






    private soopl_Package soopl_package;




    private List<soopl_Package> soopl_packages;


    public soopl_Package(
    ) {
        super(
        );
        this.soopl_packages = new ArrayList<>();
    }

    public soopl_Package(
        ArrayList<soopl_Package> soopl_packages    ) {
        this.soopl_packages = soopl_packages;
    }


    public soopl_Package getSoopl_package() {
        return soopl_package;
    }

    public void setSoopl_package(soopl_Package soopl_package) {
        this.soopl_package = soopl_package;
    }
    public List<soopl_Package> getSoopl_packages() {
        return soopl_packages;
    }

    public void addSoopl_package(Soopl_package soopl_package) {
        this.soopl_packages.add(soopl_package);
    }

}