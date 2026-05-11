





import java.util.List;
import java.util.ArrayList;

public class aadl2_GlobalNamespace extends Namespace {






    private List<aadl2_PropertySet> aadl2_propertysets;


    public aadl2_GlobalNamespace(
    ) {
        super(
        );
        this.aadl2_propertysets = new ArrayList<>();
    }

    public aadl2_GlobalNamespace(
        ArrayList<aadl2_PropertySet> aadl2_propertysets    ) {
        this.aadl2_propertysets = aadl2_propertysets;
    }


    public List<aadl2_PropertySet> getAadl2_propertysets() {
        return aadl2_propertysets;
    }

    public void addAadl2_propertyset(Aadl2_propertyset aadl2_propertyset) {
        this.aadl2_propertysets.add(aadl2_propertyset);
    }

}