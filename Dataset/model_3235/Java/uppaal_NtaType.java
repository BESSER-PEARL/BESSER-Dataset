





import java.util.List;
import java.util.ArrayList;

public class uppaal_NtaType  {

    private String system;
    private String imports;
    private String declaration;
    private String instantiation;





    private uppaal_DocumentRoot uppaal_documentroot;


    public uppaal_NtaType(
        String system,        String imports,        String declaration,        String instantiation    ) {
        this.system = system;
        this.imports = imports;
        this.declaration = declaration;
        this.instantiation = instantiation;
    }


    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }
    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }
    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }
    public String getInstantiation() {
        return instantiation;
    }

    public void setInstantiation(String instantiation) {
        this.instantiation = instantiation;
    }

    public uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }

}