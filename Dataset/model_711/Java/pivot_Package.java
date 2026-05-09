





import java.util.List;
import java.util.ArrayList;

public class pivot_Package extends Namespace, TemplateableElement {

    private String nsPrefix;
    private String nsURI;





    private pivot_Package pivot_package;




    private List<pivot_Package> pivot_packages;




    private List<pivot_Package> pivot_packages;


    public pivot_Package(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.pivot_packages = new ArrayList<>();
        this.pivot_packages = new ArrayList<>();
    }

    public pivot_Package(
        String nsPrefix,        String nsURI        ArrayList<pivot_Package> pivot_packages,        ArrayList<pivot_Package> pivot_packages    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.pivot_packages = pivot_packages;
        this.pivot_packages = pivot_packages;
    }

    public String getNsprefix() {
        return nsPrefix;
    }

    public void setNsprefix(String nsPrefix) {
        this.nsPrefix = nsPrefix;
    }
    public String getNsuri() {
        return nsURI;
    }

    public void setNsuri(String nsURI) {
        this.nsURI = nsURI;
    }

    public pivot_Package getPivot_package() {
        return pivot_package;
    }

    public void setPivot_package(pivot_Package pivot_package) {
        this.pivot_package = pivot_package;
    }
    public List<pivot_Package> getPivot_packages() {
        return pivot_packages;
    }

    public void addPivot_package(Pivot_package pivot_package) {
        this.pivot_packages.add(pivot_package);
    }
    public List<pivot_Package> getPivot_packages() {
        return pivot_packages;
    }

    public void addPivot_package(Pivot_package pivot_package) {
        this.pivot_packages.add(pivot_package);
    }

}