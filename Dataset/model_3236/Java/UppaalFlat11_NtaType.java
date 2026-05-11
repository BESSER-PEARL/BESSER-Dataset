





import java.util.List;
import java.util.ArrayList;

public class UppaalFlat11_NtaType  {

    private String declaration;
    private String imports;
    private String instantiation;
    private String system;





    private UppaalFlat11_DocumentRoot uppaalflat11_documentroot;




    private List<UppaalFlat11_TemplateType> uppaalflat11_templatetypes;


    public UppaalFlat11_NtaType(
        String declaration,        String imports,        String instantiation,        String system    ) {
        this.declaration = declaration;
        this.imports = imports;
        this.instantiation = instantiation;
        this.system = system;
        this.uppaalflat11_templatetypes = new ArrayList<>();
    }

    public UppaalFlat11_NtaType(
        String declaration,        String imports,        String instantiation,        String system        ArrayList<UppaalFlat11_TemplateType> uppaalflat11_templatetypes    ) {
        this.declaration = declaration;
        this.imports = imports;
        this.instantiation = instantiation;
        this.system = system;
        this.uppaalflat11_templatetypes = uppaalflat11_templatetypes;
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

    public UppaalFlat11_DocumentRoot getUppaalflat11_documentroot() {
        return uppaalflat11_documentroot;
    }

    public void setUppaalflat11_documentroot(UppaalFlat11_DocumentRoot uppaalflat11_documentroot) {
        this.uppaalflat11_documentroot = uppaalflat11_documentroot;
    }
    public List<UppaalFlat11_TemplateType> getUppaalflat11_templatetypes() {
        return uppaalflat11_templatetypes;
    }

    public void addUppaalflat11_templatetype(Uppaalflat11_templatetype uppaalflat11_templatetype) {
        this.uppaalflat11_templatetypes.add(uppaalflat11_templatetype);
    }

}