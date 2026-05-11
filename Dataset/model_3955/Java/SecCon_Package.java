





import java.util.List;
import java.util.ArrayList;

public class SecCon_Package extends NamedElement {






    private List<SecCon_Package> seccon_packages;




    private SecCon_Package seccon_package;


    public SecCon_Package(
    ) {
        super(
        );
        this.seccon_packages = new ArrayList<>();
    }

    public SecCon_Package(
        ArrayList<SecCon_Package> seccon_packages    ) {
        this.seccon_packages = seccon_packages;
    }


    public List<SecCon_Package> getSeccon_packages() {
        return seccon_packages;
    }

    public void addSeccon_package(Seccon_package seccon_package) {
        this.seccon_packages.add(seccon_package);
    }
    public SecCon_Package getSeccon_package() {
        return seccon_package;
    }

    public void setSeccon_package(SecCon_Package seccon_package) {
        this.seccon_package = seccon_package;
    }

}