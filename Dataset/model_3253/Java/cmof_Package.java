





import java.util.List;
import java.util.ArrayList;

public class cmof_Package extends PackageableElement, Namespace {

    private String uRI;





    private cmof_Package cmof_package;




    private List<cmof_Package> cmof_packages;


    public cmof_Package(
        String uRI    ) {
        super(
        );
        this.uRI = uRI;
        this.cmof_packages = new ArrayList<>();
    }

    public cmof_Package(
        String uRI        ArrayList<cmof_Package> cmof_packages    ) {
        this.uRI = uRI;
        this.cmof_packages = cmof_packages;
    }

    public String getUri() {
        return uRI;
    }

    public void setUri(String uRI) {
        this.uRI = uRI;
    }

    public cmof_Package getCmof_package() {
        return cmof_package;
    }

    public void setCmof_package(cmof_Package cmof_package) {
        this.cmof_package = cmof_package;
    }
    public List<cmof_Package> getCmof_packages() {
        return cmof_packages;
    }

    public void addCmof_package(Cmof_package cmof_package) {
        this.cmof_packages.add(cmof_package);
    }

}