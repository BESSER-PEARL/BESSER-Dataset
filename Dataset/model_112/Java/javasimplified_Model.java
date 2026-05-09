





import java.util.List;
import java.util.ArrayList;

public class javasimplified_Model extends NamedElement {






    private List<javasimplified_Package> javasimplified_packages;


    public javasimplified_Model(
    ) {
        super(
        );
        this.javasimplified_packages = new ArrayList<>();
    }

    public javasimplified_Model(
        ArrayList<javasimplified_Package> javasimplified_packages    ) {
        this.javasimplified_packages = javasimplified_packages;
    }


    public List<javasimplified_Package> getJavasimplified_packages() {
        return javasimplified_packages;
    }

    public void addJavasimplified_package(Javasimplified_package javasimplified_package) {
        this.javasimplified_packages.add(javasimplified_package);
    }

}