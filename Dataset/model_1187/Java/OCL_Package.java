





import java.util.List;
import java.util.ArrayList;

public class OCL_Package extends NamedElement {

    private String uri;





    private List<Package> packages;


    public OCL_Package(
        String uri    ) {
        super(
        );
        this.uri = uri;
        this.packages = new ArrayList<>();
    }

    public OCL_Package(
        String uri        ArrayList<Package> packages    ) {
        this.uri = uri;
        this.packages = packages;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public List<Package> getPackages() {
        return packages;
    }

    public void addPackage(Package package) {
        this.packages.add(package);
    }

}