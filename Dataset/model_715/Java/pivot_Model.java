





import java.util.List;
import java.util.ArrayList;

public class pivot_Model extends Namespace {

    private String externalURI;





    private List<pivot_Import> pivot_imports;




    private pivot_CompleteModel pivot_completemodel;




    private List<pivot_Package> pivot_packages;


    public pivot_Model(
        String externalURI    ) {
        super(
        );
        this.externalURI = externalURI;
        this.pivot_imports = new ArrayList<>();
        this.pivot_packages = new ArrayList<>();
    }

    public pivot_Model(
        String externalURI        ArrayList<pivot_Import> pivot_imports,        ArrayList<pivot_Package> pivot_packages    ) {
        this.externalURI = externalURI;
        this.pivot_imports = pivot_imports;
        this.pivot_packages = pivot_packages;
    }

    public String getExternaluri() {
        return externalURI;
    }

    public void setExternaluri(String externalURI) {
        this.externalURI = externalURI;
    }

    public List<pivot_Import> getPivot_imports() {
        return pivot_imports;
    }

    public void addPivot_import(Pivot_import pivot_import) {
        this.pivot_imports.add(pivot_import);
    }
    public pivot_CompleteModel getPivot_completemodel() {
        return pivot_completemodel;
    }

    public void setPivot_completemodel(pivot_CompleteModel pivot_completemodel) {
        this.pivot_completemodel = pivot_completemodel;
    }
    public List<pivot_Package> getPivot_packages() {
        return pivot_packages;
    }

    public void addPivot_package(Pivot_package pivot_package) {
        this.pivot_packages.add(pivot_package);
    }

}