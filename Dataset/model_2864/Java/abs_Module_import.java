





import java.util.List;
import java.util.ArrayList;

public class abs_Module_import extends Namespace_modifier {

    private String importedNamespace;
    private String name;





    private abs_Module_decl abs_module_decl;


    public abs_Module_import(
        String importedNamespace,        String name    ) {
        super(
        );
        this.importedNamespace = importedNamespace;
        this.name = name;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public abs_Module_decl getAbs_module_decl() {
        return abs_module_decl;
    }

    public void setAbs_module_decl(abs_Module_decl abs_module_decl) {
        this.abs_module_decl = abs_module_decl;
    }

}