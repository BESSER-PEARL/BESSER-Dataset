





import java.util.List;
import java.util.ArrayList;

public class EMOF_Package extends NamedElement {

    private String uri;





    private List<Type> types;




    private List<Package> packages;




    private Package package;


    public EMOF_Package(
        String uri    ) {
        super(
        );
        this.uri = uri;
        this.types = new ArrayList<>();
        this.packages = new ArrayList<>();
    }

    public EMOF_Package(
        String uri        ArrayList<Type> types,        ArrayList<Package> packages    ) {
        this.uri = uri;
        this.types = types;
        this.packages = packages;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public List<Package> getPackages() {
        return packages;
    }

    public void addPackage(Package package) {
        this.packages.add(package);
    }
    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }

}