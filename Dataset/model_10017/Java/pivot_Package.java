





import java.util.List;
import java.util.ArrayList;

public class pivot_Package extends Namespace {

    private String nsPrefix;
    private String URI;





    private List<pivot_Package> pivot_packages;




    private List<pivot_Class> pivot_classs;




    private pivot_Model pivot_model;




    private pivot_Package pivot_package;




    private List<pivot_Package> pivot_packages;




    private pivot_Class pivot_class;


    public pivot_Package(
        String nsPrefix,        String URI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.URI = URI;
        this.pivot_packages = new ArrayList<>();
        this.pivot_classs = new ArrayList<>();
        this.pivot_packages = new ArrayList<>();
    }

    public pivot_Package(
        String nsPrefix,        String URI        ArrayList<pivot_Package> pivot_packages,        ArrayList<pivot_Class> pivot_classs,        ArrayList<pivot_Package> pivot_packages    ) {
        this.nsPrefix = nsPrefix;
        this.URI = URI;
        this.pivot_packages = pivot_packages;
        this.pivot_classs = pivot_classs;
        this.pivot_packages = pivot_packages;
    }

    public String getNsprefix() {
        return nsPrefix;
    }

    public void setNsprefix(String nsPrefix) {
        this.nsPrefix = nsPrefix;
    }
    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }

    public List<pivot_Package> getPivot_packages() {
        return pivot_packages;
    }

    public void addPivot_package(Pivot_package pivot_package) {
        this.pivot_packages.add(pivot_package);
    }
    public List<pivot_Class> getPivot_classs() {
        return pivot_classs;
    }

    public void addPivot_class(Pivot_class pivot_class) {
        this.pivot_classs.add(pivot_class);
    }
    public pivot_Model getPivot_model() {
        return pivot_model;
    }

    public void setPivot_model(pivot_Model pivot_model) {
        this.pivot_model = pivot_model;
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
    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
    }

}