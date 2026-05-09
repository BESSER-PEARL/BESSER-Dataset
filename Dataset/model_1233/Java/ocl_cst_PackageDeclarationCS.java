





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_PackageDeclarationCS extends CSTNode {






    private List<ContextDeclCS> contextdeclcss;




    private PackageDeclarationCS packagedeclarationcs;


    public ocl_cst_PackageDeclarationCS(
    ) {
        super(
        );
        this.contextdeclcss = new ArrayList<>();
    }

    public ocl_cst_PackageDeclarationCS(
        ArrayList<ContextDeclCS> contextdeclcss    ) {
        this.contextdeclcss = contextdeclcss;
    }


    public List<ContextDeclCS> getContextdeclcss() {
        return contextdeclcss;
    }

    public void addContextdeclcs(Contextdeclcs contextdeclcs) {
        this.contextdeclcss.add(contextdeclcs);
    }
    public PackageDeclarationCS getPackagedeclarationcs() {
        return packagedeclarationcs;
    }

    public void setPackagedeclarationcs(PackageDeclarationCS packagedeclarationcs) {
        this.packagedeclarationcs = packagedeclarationcs;
    }

}