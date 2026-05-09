





import java.util.List;
import java.util.ArrayList;

public class pivot_Root extends Namespace {

    private String externalURI;





    private List<pivot_Package> pivot_packages;




    private List<pivot_Import> pivot_imports;


    public pivot_Root(
        String externalURI    ) {
        super(
        );
        this.externalURI = externalURI;
        this.pivot_packages = new ArrayList<>();
        this.pivot_imports = new ArrayList<>();
    }

    public pivot_Root(
        String externalURI        ArrayList<pivot_Package> pivot_packages,        ArrayList<pivot_Import> pivot_imports    ) {
        this.externalURI = externalURI;
        this.pivot_packages = pivot_packages;
        this.pivot_imports = pivot_imports;
    }

    public String getExternaluri() {
        return externalURI;
    }

    public void setExternaluri(String externalURI) {
        this.externalURI = externalURI;
    }

    public List<pivot_Package> getPivot_packages() {
        return pivot_packages;
    }

    public void addPivot_package(Pivot_package pivot_package) {
        this.pivot_packages.add(pivot_package);
    }
    public List<pivot_Import> getPivot_imports() {
        return pivot_imports;
    }

    public void addPivot_import(Pivot_import pivot_import) {
        this.pivot_imports.add(pivot_import);
    }

}