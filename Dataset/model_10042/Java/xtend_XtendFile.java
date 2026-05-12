





import java.util.List;
import java.util.ArrayList;

public class xtend_XtendFile  {

    private String package;





    private List<xtend_XtendTypeDeclaration> xtend_xtendtypedeclarations;


    public xtend_XtendFile(
        String package    ) {
        this.package = package;
        this.xtend_xtendtypedeclarations = new ArrayList<>();
    }

    public xtend_XtendFile(
        String package        ArrayList<xtend_XtendTypeDeclaration> xtend_xtendtypedeclarations    ) {
        this.package = package;
        this.xtend_xtendtypedeclarations = xtend_xtendtypedeclarations;
    }

    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }

    public List<xtend_XtendTypeDeclaration> getXtend_xtendtypedeclarations() {
        return xtend_xtendtypedeclarations;
    }

    public void addXtend_xtendtypedeclaration(Xtend_xtendtypedeclaration xtend_xtendtypedeclaration) {
        this.xtend_xtendtypedeclarations.add(xtend_xtendtypedeclaration);
    }

}