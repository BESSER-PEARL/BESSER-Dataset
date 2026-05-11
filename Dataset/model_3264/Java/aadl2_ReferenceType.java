





import java.util.List;
import java.util.ArrayList;

public class aadl2_ReferenceType extends NonListType {






    private List<aadl2_MetaclassReference> aadl2_metaclassreferences;


    public aadl2_ReferenceType(
    ) {
        super(
        );
        this.aadl2_metaclassreferences = new ArrayList<>();
    }

    public aadl2_ReferenceType(
        ArrayList<aadl2_MetaclassReference> aadl2_metaclassreferences    ) {
        this.aadl2_metaclassreferences = aadl2_metaclassreferences;
    }


    public List<aadl2_MetaclassReference> getAadl2_metaclassreferences() {
        return aadl2_metaclassreferences;
    }

    public void addAadl2_metaclassreference(Aadl2_metaclassreference aadl2_metaclassreference) {
        this.aadl2_metaclassreferences.add(aadl2_metaclassreference);
    }

}