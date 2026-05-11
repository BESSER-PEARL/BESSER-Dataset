





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_Package extends Kernel_Namespace, Kernel_PackageableElement {

    private String URI;





    private List<Package> packages;




    private Package package;




    private List<PackageableElement> packageableelements;


    public Classes_Kernel_Package(
        String URI    ) {
        super(
        );
        this.URI = URI;
        this.packages = new ArrayList<>();
        this.packageableelements = new ArrayList<>();
    }

    public Classes_Kernel_Package(
        String URI        ArrayList<Package> packages,        ArrayList<PackageableElement> packageableelements    ) {
        this.URI = URI;
        this.packages = packages;
        this.packageableelements = packageableelements;
    }

    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
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
    public List<PackageableElement> getPackageableelements() {
        return packageableelements;
    }

    public void addPackageableelement(Packageableelement packageableelement) {
        this.packageableelements.add(packageableelement);
    }

}