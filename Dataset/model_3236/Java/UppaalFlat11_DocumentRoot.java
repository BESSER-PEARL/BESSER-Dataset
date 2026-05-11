





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_DocumentRoot  {

    private String instantiation;
    private String declaration;
    private String system;
    private String imports;
    private String mixed;





    private List<UppaalFlat11_CommittedType> uppaalflat11_committedtypes;


    public UppaalFlat11_DocumentRoot(
        String instantiation,        String declaration,        String system,        String imports,        String mixed    ) {
        this.instantiation = instantiation;
        this.declaration = declaration;
        this.system = system;
        this.imports = imports;
        this.mixed = mixed;
        this.uppaalflat11_committedtypes = new ArrayList<>();
    }

    public UppaalFlat11_DocumentRoot(
        String instantiation,        String declaration,        String system,        String imports,        String mixed        ArrayList<UppaalFlat11_CommittedType> uppaalflat11_committedtypes    ) {
        this.instantiation = instantiation;
        this.declaration = declaration;
        this.system = system;
        this.imports = imports;
        this.mixed = mixed;
        this.uppaalflat11_committedtypes = uppaalflat11_committedtypes;
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

    public List<UppaalFlat11_CommittedType> getUppaalflat11_committedtypes() {
        return uppaalflat11_committedtypes;
    }

    public void addUppaalflat11_committedtype(Uppaalflat11_committedtype uppaalflat11_committedtype) {
        this.uppaalflat11_committedtypes.add(uppaalflat11_committedtype);
    }

}