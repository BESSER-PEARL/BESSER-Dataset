





import java.util.List;
import java.util.ArrayList;

public class flat11_DocumentRoot  {

    private String declaration;
    private String instantiation;
    private String system;
    private String imports;
    private String mixed;





    private List<flat11_CommittedType> flat11_committedtypes;


    public flat11_DocumentRoot(
        String declaration,        String instantiation,        String system,        String imports,        String mixed    ) {
        this.declaration = declaration;
        this.instantiation = instantiation;
        this.system = system;
        this.imports = imports;
        this.mixed = mixed;
        this.flat11_committedtypes = new ArrayList<>();
    }

    public flat11_DocumentRoot(
        String declaration,        String instantiation,        String system,        String imports,        String mixed        ArrayList<flat11_CommittedType> flat11_committedtypes    ) {
        this.declaration = declaration;
        this.instantiation = instantiation;
        this.system = system;
        this.imports = imports;
        this.mixed = mixed;
        this.flat11_committedtypes = flat11_committedtypes;
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
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<flat11_CommittedType> getFlat11_committedtypes() {
        return flat11_committedtypes;
    }

    public void addFlat11_committedtype(Flat11_committedtype flat11_committedtype) {
        this.flat11_committedtypes.add(flat11_committedtype);
    }

}