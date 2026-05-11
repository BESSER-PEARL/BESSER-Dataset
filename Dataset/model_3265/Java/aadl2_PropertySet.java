





import java.util.List;
import java.util.ArrayList;

public class aadl2_PropertySet extends ModelUnit, Namespace {






    private aadl2_GlobalNamespace aadl2_globalnamespace;




    private List<aadl2_PropertyConstant> aadl2_propertyconstants;




    private List<aadl2_Property> aadl2_propertys;




    private List<aadl2_ModelUnit> aadl2_modelunits;


    public aadl2_PropertySet(
    ) {
        super(
        );
        this.aadl2_propertyconstants = new ArrayList<>();
        this.aadl2_propertys = new ArrayList<>();
        this.aadl2_modelunits = new ArrayList<>();
    }

    public aadl2_PropertySet(
        ArrayList<aadl2_PropertyConstant> aadl2_propertyconstants,        ArrayList<aadl2_Property> aadl2_propertys,        ArrayList<aadl2_ModelUnit> aadl2_modelunits    ) {
        this.aadl2_propertyconstants = aadl2_propertyconstants;
        this.aadl2_propertys = aadl2_propertys;
        this.aadl2_modelunits = aadl2_modelunits;
    }


    public aadl2_GlobalNamespace getAadl2_globalnamespace() {
        return aadl2_globalnamespace;
    }

    public void setAadl2_globalnamespace(aadl2_GlobalNamespace aadl2_globalnamespace) {
        this.aadl2_globalnamespace = aadl2_globalnamespace;
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
    public List<aadl2_ModelUnit> getAadl2_modelunits() {
        return aadl2_modelunits;
    }

    public void addAadl2_modelunit(Aadl2_modelunit aadl2_modelunit) {
        this.aadl2_modelunits.add(aadl2_modelunit);
    }

}