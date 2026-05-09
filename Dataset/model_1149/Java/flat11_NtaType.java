





import java.util.List;
import java.util.ArrayList;

public class flat11_NtaType  {

    private String declaration;
    private String imports;
    private String instantiation;
    private String system;





    private flat11_DocumentRoot flat11_documentroot;


    public flat11_NtaType(
        String declaration,        String imports,        String instantiation,        String system    ) {
        this.declaration = declaration;
        this.imports = imports;
        this.instantiation = instantiation;
        this.system = system;
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
    public String getInstantiation() {
        return instantiation;
    }

    public void setInstantiation(String instantiation) {
        this.instantiation = instantiation;
    }
    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }

    public flat11_DocumentRoot getFlat11_documentroot() {
        return flat11_documentroot;
    }

    public void setFlat11_documentroot(flat11_DocumentRoot flat11_documentroot) {
        this.flat11_documentroot = flat11_documentroot;
    }

}