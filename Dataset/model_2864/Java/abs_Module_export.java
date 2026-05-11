





import java.util.List;
import java.util.ArrayList;

public class abs_Module_export extends Namespace_modifier {

    private String importedNamespace;
    private String anyPackage;





    private abs_Module_decl abs_module_decl;


    public abs_Module_export(
        String importedNamespace,        String anyPackage    ) {
        super(
        );
        this.importedNamespace = importedNamespace;
        this.anyPackage = anyPackage;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }
    public String getAnypackage() {
        return anyPackage;
    }

    public void setAnypackage(String anyPackage) {
        this.anyPackage = anyPackage;
    }

    public abs_Module_decl getAbs_module_decl() {
        return abs_module_decl;
    }

    public void setAbs_module_decl(abs_Module_decl abs_module_decl) {
        this.abs_module_decl = abs_module_decl;
    }

}