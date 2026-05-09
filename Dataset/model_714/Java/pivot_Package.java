





import java.util.List;
import java.util.ArrayList;

public class pivot_Package extends TemplateableElement, Namespace {

    private String nsPrefix;
    private String nsURI;





    private List<pivot_Package> pivot_packages;




    private List<pivot_Package> pivot_packages;




    private pivot_Package pivot_package;




    private List<pivot_Type> pivot_types;




    private pivot_Type pivot_type;


    public pivot_Package(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.pivot_packages = new ArrayList<>();
        this.pivot_packages = new ArrayList<>();
        this.pivot_types = new ArrayList<>();
    }

    public pivot_Package(
        String nsPrefix,        String nsURI        ArrayList<pivot_Package> pivot_packages,        ArrayList<pivot_Package> pivot_packages,        ArrayList<pivot_Type> pivot_types    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.pivot_packages = pivot_packages;
        this.pivot_packages = pivot_packages;
        this.pivot_types = pivot_types;
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
    public pivot_Package getPivot_package() {
        return pivot_package;
    }

    public void setPivot_package(pivot_Package pivot_package) {
        this.pivot_package = pivot_package;
    }
    public List<pivot_Type> getPivot_types() {
        return pivot_types;
    }

    public void addPivot_type(Pivot_type pivot_type) {
        this.pivot_types.add(pivot_type);
    }
    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }

}