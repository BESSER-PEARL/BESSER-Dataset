





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_OCLDocumentCS extends CSTNode {






    private List<PackageDeclarationCS> packagedeclarationcss;


    public ocl_cst_OCLDocumentCS(
    ) {
        super(
        );
        this.packagedeclarationcss = new ArrayList<>();
    }

    public ocl_cst_OCLDocumentCS(
        ArrayList<PackageDeclarationCS> packagedeclarationcss    ) {
        this.packagedeclarationcss = packagedeclarationcss;
    }


    public List<PackageDeclarationCS> getPackagedeclarationcss() {
        return packagedeclarationcss;
    }

    public void addPackagedeclarationcs(Packagedeclarationcs packagedeclarationcs) {
        this.packagedeclarationcss.add(packagedeclarationcs);
    }

}