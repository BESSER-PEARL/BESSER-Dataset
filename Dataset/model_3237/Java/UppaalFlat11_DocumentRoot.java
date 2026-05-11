





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_DocumentRoot  {

    private String system;
    private String declaration;
    private String mixed;
    private String instantiation;
    private String imports;





    private List<UppaalFlat11_CommittedType> uppaalflat11_committedtypes;


    public UppaalFlat11_DocumentRoot(
        String system,        String declaration,        String mixed,        String instantiation,        String imports    ) {
        this.system = system;
        this.declaration = declaration;
        this.mixed = mixed;
        this.instantiation = instantiation;
        this.imports = imports;
        this.uppaalflat11_committedtypes = new ArrayList<>();
    }

    public UppaalFlat11_DocumentRoot(
        String system,        String declaration,        String mixed,        String instantiation,        String imports        ArrayList<UppaalFlat11_CommittedType> uppaalflat11_committedtypes    ) {
        this.system = system;
        this.declaration = declaration;
        this.mixed = mixed;
        this.instantiation = instantiation;
        this.imports = imports;
        this.uppaalflat11_committedtypes = uppaalflat11_committedtypes;
    }

    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }
    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getInstantiation() {
        return instantiation;
    }

    public void setInstantiation(String instantiation) {
        this.instantiation = instantiation;
    }
    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }

    public List<UppaalFlat11_CommittedType> getUppaalflat11_committedtypes() {
        return uppaalflat11_committedtypes;
    }

    public void addUppaalflat11_committedtype(Uppaalflat11_committedtype uppaalflat11_committedtype) {
        this.uppaalflat11_committedtypes.add(uppaalflat11_committedtype);
    }

}