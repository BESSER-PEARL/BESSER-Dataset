





import java.util.List;
import java.util.ArrayList;

public class uppaal_DocumentRoot  {

    private String instantiation;
    private String mixed;
    private String imports;
    private String declaration;
    private String system;





    private List<uppaal_CommittedType> uppaal_committedtypes;




    private List<uppaal_EStringToStringMapEntry> uppaal_estringtostringmapentrys;




    private List<uppaal_LabelType> uppaal_labeltypes;




    private List<uppaal_InitType> uppaal_inittypes;




    private List<uppaal_EStringToStringMapEntry> uppaal_estringtostringmapentrys;


    public uppaal_DocumentRoot(
        String instantiation,        String mixed,        String imports,        String declaration,        String system    ) {
        this.instantiation = instantiation;
        this.mixed = mixed;
        this.imports = imports;
        this.declaration = declaration;
        this.system = system;
        this.uppaal_committedtypes = new ArrayList<>();
        this.uppaal_estringtostringmapentrys = new ArrayList<>();
        this.uppaal_labeltypes = new ArrayList<>();
        this.uppaal_inittypes = new ArrayList<>();
        this.uppaal_estringtostringmapentrys = new ArrayList<>();
    }

    public uppaal_DocumentRoot(
        String instantiation,        String mixed,        String imports,        String declaration,        String system        ArrayList<uppaal_CommittedType> uppaal_committedtypes,        ArrayList<uppaal_EStringToStringMapEntry> uppaal_estringtostringmapentrys,        ArrayList<uppaal_LabelType> uppaal_labeltypes,        ArrayList<uppaal_InitType> uppaal_inittypes,        ArrayList<uppaal_EStringToStringMapEntry> uppaal_estringtostringmapentrys    ) {
        this.instantiation = instantiation;
        this.mixed = mixed;
        this.imports = imports;
        this.declaration = declaration;
        this.system = system;
        this.uppaal_committedtypes = uppaal_committedtypes;
        this.uppaal_estringtostringmapentrys = uppaal_estringtostringmapentrys;
        this.uppaal_labeltypes = uppaal_labeltypes;
        this.uppaal_inittypes = uppaal_inittypes;
        this.uppaal_estringtostringmapentrys = uppaal_estringtostringmapentrys;
    }

    public String getInstantiation() {
        return instantiation;
    }

    public void setInstantiation(String instantiation) {
        this.instantiation = instantiation;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
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
    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }

    public List<uppaal_CommittedType> getUppaal_committedtypes() {
        return uppaal_committedtypes;
    }

    public void addUppaal_committedtype(Uppaal_committedtype uppaal_committedtype) {
        this.uppaal_committedtypes.add(uppaal_committedtype);
    }
    public List<uppaal_EStringToStringMapEntry> getUppaal_estringtostringmapentrys() {
        return uppaal_estringtostringmapentrys;
    }

    public void addUppaal_estringtostringmapentry(Uppaal_estringtostringmapentry uppaal_estringtostringmapentry) {
        this.uppaal_estringtostringmapentrys.add(uppaal_estringtostringmapentry);
    }
    public List<uppaal_LabelType> getUppaal_labeltypes() {
        return uppaal_labeltypes;
    }

    public void addUppaal_labeltype(Uppaal_labeltype uppaal_labeltype) {
        this.uppaal_labeltypes.add(uppaal_labeltype);
    }
    public List<uppaal_InitType> getUppaal_inittypes() {
        return uppaal_inittypes;
    }

    public void addUppaal_inittype(Uppaal_inittype uppaal_inittype) {
        this.uppaal_inittypes.add(uppaal_inittype);
    }
    public List<uppaal_EStringToStringMapEntry> getUppaal_estringtostringmapentrys() {
        return uppaal_estringtostringmapentrys;
    }

    public void addUppaal_estringtostringmapentry(Uppaal_estringtostringmapentry uppaal_estringtostringmapentry) {
        this.uppaal_estringtostringmapentrys.add(uppaal_estringtostringmapentry);
    }

}