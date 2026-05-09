





import java.util.List;
import java.util.ArrayList;

public class pivot_Package extends Namespace {

    private String nsPrefix;
    private String URI;





    private pivot_InstanceSpecification pivot_instancespecification;




    private List<pivot_Class> pivot_classs;




    private List<pivot_InstanceSpecification> pivot_instancespecifications;




    private pivot_Package pivot_package;




    private pivot_Package pivot_package;




    private pivot_Class pivot_class;




    private List<pivot_Package> pivot_packages;




    private pivot_CompletePackage pivot_completepackage;


    public pivot_Package(
        String nsPrefix,        String URI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.URI = URI;
        this.pivot_classs = new ArrayList<>();
        this.pivot_instancespecifications = new ArrayList<>();
        this.pivot_packages = new ArrayList<>();
    }

    public pivot_Package(
        String nsPrefix,        String URI        ArrayList<pivot_Class> pivot_classs,        ArrayList<pivot_InstanceSpecification> pivot_instancespecifications,        ArrayList<pivot_Package> pivot_packages    ) {
        this.nsPrefix = nsPrefix;
        this.URI = URI;
        this.pivot_classs = pivot_classs;
        this.pivot_instancespecifications = pivot_instancespecifications;
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

    public pivot_InstanceSpecification getPivot_instancespecification() {
        return pivot_instancespecification;
    }

    public void setPivot_instancespecification(pivot_InstanceSpecification pivot_instancespecification) {
        this.pivot_instancespecification = pivot_instancespecification;
    }
    public List<pivot_Class> getPivot_classs() {
        return pivot_classs;
    }

    public void addPivot_class(Pivot_class pivot_class) {
        this.pivot_classs.add(pivot_class);
    }
    public List<pivot_InstanceSpecification> getPivot_instancespecifications() {
        return pivot_instancespecifications;
    }

    public void addPivot_instancespecification(Pivot_instancespecification pivot_instancespecification) {
        this.pivot_instancespecifications.add(pivot_instancespecification);
    }
    public pivot_Package getPivot_package() {
        return pivot_package;
    }

    public void setPivot_package(pivot_Package pivot_package) {
        this.pivot_package = pivot_package;
    }
    public pivot_Package getPivot_package() {
        return pivot_package;
    }

    public void setPivot_package(pivot_Package pivot_package) {
        this.pivot_package = pivot_package;
    }
    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
    }
    public List<pivot_Package> getPivot_packages() {
        return pivot_packages;
    }

    public void addPivot_package(Pivot_package pivot_package) {
        this.pivot_packages.add(pivot_package);
    }
    public pivot_CompletePackage getPivot_completepackage() {
        return pivot_completepackage;
    }

    public void setPivot_completepackage(pivot_CompletePackage pivot_completepackage) {
        this.pivot_completepackage = pivot_completepackage;
    }

}