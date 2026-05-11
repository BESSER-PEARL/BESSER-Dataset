





import java.util.List;
import java.util.ArrayList;

public class aadl2_PropertySet extends Namespace {

    private String imports;
    private String contents;





    private List<aadl2_PropertyConstant> aadl2_propertyconstants;




    private List<aadl2_Property> aadl2_propertys;




    private aadl2_PackageSection aadl2_packagesection;




    private aadl2_PropertySet aadl2_propertyset;




    private aadl2_GlobalNamespace aadl2_globalnamespace;




    private List<aadl2_PropertyType> aadl2_propertytypes;




    private List<aadl2_AadlPackage> aadl2_aadlpackages;


    public aadl2_PropertySet(
        String imports,        String contents    ) {
        super(
        );
        this.imports = imports;
        this.contents = contents;
        this.aadl2_propertyconstants = new ArrayList<>();
        this.aadl2_propertys = new ArrayList<>();
        this.aadl2_propertytypes = new ArrayList<>();
        this.aadl2_aadlpackages = new ArrayList<>();
    }

    public aadl2_PropertySet(
        String imports,        String contents        ArrayList<aadl2_PropertyConstant> aadl2_propertyconstants,        ArrayList<aadl2_Property> aadl2_propertys,        ArrayList<aadl2_PropertyType> aadl2_propertytypes,        ArrayList<aadl2_AadlPackage> aadl2_aadlpackages    ) {
        this.imports = imports;
        this.contents = contents;
        this.aadl2_propertyconstants = aadl2_propertyconstants;
        this.aadl2_propertys = aadl2_propertys;
        this.aadl2_propertytypes = aadl2_propertytypes;
        this.aadl2_aadlpackages = aadl2_aadlpackages;
    }

    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }
    public String getContents() {
        return contents;
    }

    public void setContents(String contents) {
        this.contents = contents;
    }

    public List<aadl2_PropertyConstant> getAadl2_propertyconstants() {
        return aadl2_propertyconstants;
    }

    public void addAadl2_propertyconstant(Aadl2_propertyconstant aadl2_propertyconstant) {
        this.aadl2_propertyconstants.add(aadl2_propertyconstant);
    }
    public List<aadl2_Property> getAadl2_propertys() {
        return aadl2_propertys;
    }

    public void addAadl2_property(Aadl2_property aadl2_property) {
        this.aadl2_propertys.add(aadl2_property);
    }
    public aadl2_PackageSection getAadl2_packagesection() {
        return aadl2_packagesection;
    }

    public void setAadl2_packagesection(aadl2_PackageSection aadl2_packagesection) {
        this.aadl2_packagesection = aadl2_packagesection;
    }
    public aadl2_PropertySet getAadl2_propertyset() {
        return aadl2_propertyset;
    }

    public void setAadl2_propertyset(aadl2_PropertySet aadl2_propertyset) {
        this.aadl2_propertyset = aadl2_propertyset;
    }
    public aadl2_GlobalNamespace getAadl2_globalnamespace() {
        return aadl2_globalnamespace;
    }

    public void setAadl2_globalnamespace(aadl2_GlobalNamespace aadl2_globalnamespace) {
        this.aadl2_globalnamespace = aadl2_globalnamespace;
    }
    public List<aadl2_PropertyType> getAadl2_propertytypes() {
        return aadl2_propertytypes;
    }

    public void addAadl2_propertytype(Aadl2_propertytype aadl2_propertytype) {
        this.aadl2_propertytypes.add(aadl2_propertytype);
    }
    public List<aadl2_AadlPackage> getAadl2_aadlpackages() {
        return aadl2_aadlpackages;
    }

    public void addAadl2_aadlpackage(Aadl2_aadlpackage aadl2_aadlpackage) {
        this.aadl2_aadlpackages.add(aadl2_aadlpackage);
    }

}