





import java.util.List;
import java.util.ArrayList;

public class aadl2_RecordValue extends PropertyValue {






    private List<aadl2_BasicPropertyAssociation> aadl2_basicpropertyassociations;


    public aadl2_RecordValue(
    ) {
        super(
        );
        this.aadl2_basicpropertyassociations = new ArrayList<>();
    }

    public aadl2_RecordValue(
        ArrayList<aadl2_BasicPropertyAssociation> aadl2_basicpropertyassociations    ) {
        this.aadl2_basicpropertyassociations = aadl2_basicpropertyassociations;
    }


    public List<aadl2_BasicPropertyAssociation> getAadl2_basicpropertyassociations() {
        return aadl2_basicpropertyassociations;
    }

    public void addAadl2_basicpropertyassociation(Aadl2_basicpropertyassociation aadl2_basicpropertyassociation) {
        this.aadl2_basicpropertyassociations.add(aadl2_basicpropertyassociation);
    }

}