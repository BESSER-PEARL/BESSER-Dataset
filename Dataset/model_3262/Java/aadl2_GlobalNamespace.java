





import java.util.List;
import java.util.ArrayList;

public class aadl2_GlobalNamespace extends Namespace {






    private List<aadl2_PropertySet> aadl2_propertysets;




    private List<aadl2_PublicPackageSection> aadl2_publicpackagesections;


    public aadl2_GlobalNamespace(
    ) {
        super(
        );
        this.aadl2_propertysets = new ArrayList<>();
        this.aadl2_publicpackagesections = new ArrayList<>();
    }

    public aadl2_GlobalNamespace(
        ArrayList<aadl2_PropertySet> aadl2_propertysets,        ArrayList<aadl2_PublicPackageSection> aadl2_publicpackagesections    ) {
        this.aadl2_propertysets = aadl2_propertysets;
        this.aadl2_publicpackagesections = aadl2_publicpackagesections;
    }


    public List<aadl2_PropertySet> getAadl2_propertysets() {
        return aadl2_propertysets;
    }

    public void addAadl2_propertyset(Aadl2_propertyset aadl2_propertyset) {
        this.aadl2_propertysets.add(aadl2_propertyset);
    }
    public List<aadl2_PublicPackageSection> getAadl2_publicpackagesections() {
        return aadl2_publicpackagesections;
    }

    public void addAadl2_publicpackagesection(Aadl2_publicpackagesection aadl2_publicpackagesection) {
        this.aadl2_publicpackagesections.add(aadl2_publicpackagesection);
    }

}