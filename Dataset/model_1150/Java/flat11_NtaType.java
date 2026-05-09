





import java.util.List;
import java.util.ArrayList;

public class flat11_NtaType  {

    private String system;
    private String instantiation;
    private String declaration;
    private String imports;





    private flat11_DocumentRoot flat11_documentroot;


    public flat11_NtaType(
        String system,        String instantiation,        String declaration,        String imports    ) {
        this.system = system;
        this.instantiation = instantiation;
        this.declaration = declaration;
        this.imports = imports;
    }


    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }
    public String getInstantiation() {
        return instantiation;
    }

    public void setInstantiation(String instantiation) {
        this.instantiation = instantiation;
    }
    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }
    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }

    public flat11_DocumentRoot getFlat11_documentroot() {
        return flat11_documentroot;
    }

    public void setFlat11_documentroot(flat11_DocumentRoot flat11_documentroot) {
        this.flat11_documentroot = flat11_documentroot;
    }

}