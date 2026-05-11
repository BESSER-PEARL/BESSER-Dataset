





import java.util.List;
import java.util.ArrayList;

public class sooml_Package extends NamedElement {






    private List<sooml_Package> sooml_packages;




    private sooml_Package sooml_package;


    public sooml_Package(
    ) {
        super(
        );
        this.sooml_packages = new ArrayList<>();
    }

    public sooml_Package(
        ArrayList<sooml_Package> sooml_packages    ) {
        this.sooml_packages = sooml_packages;
    }


    public List<sooml_Package> getSooml_packages() {
        return sooml_packages;
    }

    public void addSooml_package(Sooml_package sooml_package) {
        this.sooml_packages.add(sooml_package);
    }
    public sooml_Package getSooml_package() {
        return sooml_package;
    }

    public void setSooml_package(sooml_Package sooml_package) {
        this.sooml_package = sooml_package;
    }

}