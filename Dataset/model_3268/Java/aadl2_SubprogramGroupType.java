





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramGroupType extends SubprogramGroupClassifier, ComponentType, CallContext {






    private List<aadl2_SubprogramAccess> aadl2_subprogramaccesss;


    public aadl2_SubprogramGroupType(
    ) {
        super(
        );
        this.aadl2_subprogramaccesss = new ArrayList<>();
    }

    public aadl2_SubprogramGroupType(
        ArrayList<aadl2_SubprogramAccess> aadl2_subprogramaccesss    ) {
        this.aadl2_subprogramaccesss = aadl2_subprogramaccesss;
    }


    public List<aadl2_SubprogramAccess> getAadl2_subprogramaccesss() {
        return aadl2_subprogramaccesss;
    }

    public void addAadl2_subprogramaccess(Aadl2_subprogramaccess aadl2_subprogramaccess) {
        this.aadl2_subprogramaccesss.add(aadl2_subprogramaccess);
    }

}