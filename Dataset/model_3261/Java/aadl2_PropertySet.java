





import java.util.List;
import java.util.ArrayList;

public class aadl2_PropertySet extends Namespace {

    private String imports;
    private String contents;





    private List<aadl2_AadlPackage> aadl2_aadlpackages;




    private List<aadl2_PropertySet> aadl2_propertysets;




    private List<aadl2_Property> aadl2_propertys;


    public aadl2_PropertySet(
        String imports,        String contents    ) {
        super(
        );
        this.imports = imports;
        this.contents = contents;
        this.aadl2_aadlpackages = new ArrayList<>();
        this.aadl2_propertysets = new ArrayList<>();
        this.aadl2_propertys = new ArrayList<>();
    }

    public aadl2_PropertySet(
        String imports,        String contents        ArrayList<aadl2_AadlPackage> aadl2_aadlpackages,        ArrayList<aadl2_PropertySet> aadl2_propertysets,        ArrayList<aadl2_Property> aadl2_propertys    ) {
        this.imports = imports;
        this.contents = contents;
        this.aadl2_aadlpackages = aadl2_aadlpackages;
        this.aadl2_propertysets = aadl2_propertysets;
        this.aadl2_propertys = aadl2_propertys;
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

    public List<aadl2_AadlPackage> getAadl2_aadlpackages() {
        return aadl2_aadlpackages;
    }

    public void addAadl2_aadlpackage(Aadl2_aadlpackage aadl2_aadlpackage) {
        this.aadl2_aadlpackages.add(aadl2_aadlpackage);
    }
    public List<aadl2_PropertySet> getAadl2_propertysets() {
        return aadl2_propertysets;
    }

    public void addAadl2_propertyset(Aadl2_propertyset aadl2_propertyset) {
        this.aadl2_propertysets.add(aadl2_propertyset);
    }
    public List<aadl2_Property> getAadl2_propertys() {
        return aadl2_propertys;
    }

    public void addAadl2_property(Aadl2_property aadl2_property) {
        this.aadl2_propertys.add(aadl2_property);
    }

}