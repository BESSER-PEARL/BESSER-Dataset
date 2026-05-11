





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramGroupType extends CallContext, SubprogramGroupClassifier, ComponentType {






    private List<aadl2_SubprogramGroupAccess> aadl2_subprogramgroupaccesss;


    public aadl2_SubprogramGroupType(
    ) {
        super(
        );
        this.aadl2_subprogramgroupaccesss = new ArrayList<>();
    }

    public aadl2_SubprogramGroupType(
        ArrayList<aadl2_SubprogramGroupAccess> aadl2_subprogramgroupaccesss    ) {
        this.aadl2_subprogramgroupaccesss = aadl2_subprogramgroupaccesss;
    }


    public List<aadl2_SubprogramGroupAccess> getAadl2_subprogramgroupaccesss() {
        return aadl2_subprogramgroupaccesss;
    }

    public void addAadl2_subprogramgroupaccess(Aadl2_subprogramgroupaccess aadl2_subprogramgroupaccess) {
        this.aadl2_subprogramgroupaccesss.add(aadl2_subprogramgroupaccess);
    }

}