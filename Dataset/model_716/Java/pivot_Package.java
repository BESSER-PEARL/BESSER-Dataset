





import java.util.List;
import java.util.ArrayList;

public class pivot_Package extends Namespace {

    private String nsPrefix;
    private String URI;





    private pivot_ProfileApplication pivot_profileapplication;




    private pivot_Class pivot_class;




    private pivot_InstanceSpecification pivot_instancespecification;




    private pivot_CompletePackage pivot_completepackage;




    private pivot_Package pivot_package;




    private List<pivot_InstanceSpecification> pivot_instancespecifications;




    private pivot_Package pivot_package;




    private List<pivot_ProfileApplication> pivot_profileapplications;




    private List<pivot_Class> pivot_classs;




    private pivot_Package pivot_package;


    public pivot_Package(
        String nsPrefix,        String URI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.URI = URI;
        this.pivot_instancespecifications = new ArrayList<>();
        this.pivot_profileapplications = new ArrayList<>();
        this.pivot_classs = new ArrayList<>();
    }

    public pivot_Package(
        String nsPrefix,        String URI        ArrayList<pivot_InstanceSpecification> pivot_instancespecifications,        ArrayList<pivot_ProfileApplication> pivot_profileapplications,        ArrayList<pivot_Class> pivot_classs    ) {
        this.nsPrefix = nsPrefix;
        this.URI = URI;
        this.pivot_instancespecifications = pivot_instancespecifications;
        this.pivot_profileapplications = pivot_profileapplications;
        this.pivot_classs = pivot_classs;
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

    public pivot_ProfileApplication getPivot_profileapplication() {
        return pivot_profileapplication;
    }

    public void setPivot_profileapplication(pivot_ProfileApplication pivot_profileapplication) {
        this.pivot_profileapplication = pivot_profileapplication;
    }
    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
    }
    public pivot_InstanceSpecification getPivot_instancespecification() {
        return pivot_instancespecification;
    }

    public void setPivot_instancespecification(pivot_InstanceSpecification pivot_instancespecification) {
        this.pivot_instancespecification = pivot_instancespecification;
    }
    public pivot_CompletePackage getPivot_completepackage() {
        return pivot_completepackage;
    }

    public void setPivot_completepackage(pivot_CompletePackage pivot_completepackage) {
        this.pivot_completepackage = pivot_completepackage;
    }
    public pivot_Package getPivot_package() {
        return pivot_package;
    }

    public void setPivot_package(pivot_Package pivot_package) {
        this.pivot_package = pivot_package;
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
    public List<pivot_ProfileApplication> getPivot_profileapplications() {
        return pivot_profileapplications;
    }

    public void addPivot_profileapplication(Pivot_profileapplication pivot_profileapplication) {
        this.pivot_profileapplications.add(pivot_profileapplication);
    }
    public List<pivot_Class> getPivot_classs() {
        return pivot_classs;
    }

    public void addPivot_class(Pivot_class pivot_class) {
        this.pivot_classs.add(pivot_class);
    }
    public pivot_Package getPivot_package() {
        return pivot_package;
    }

    public void setPivot_package(pivot_Package pivot_package) {
        this.pivot_package = pivot_package;
    }

}