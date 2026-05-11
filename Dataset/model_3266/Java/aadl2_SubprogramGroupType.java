





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramGroupType extends CallContext, ComponentType, SubprogramGroupClassifier {






    private List<aadl2_SubprogramGroupAccess> aadl2_subprogramgroupaccesss;




    private List<aadl2_SubprogramAccess> aadl2_subprogramaccesss;


    public aadl2_SubprogramGroupType(
    ) {
        super(
        );
        this.aadl2_subprogramgroupaccesss = new ArrayList<>();
        this.aadl2_subprogramaccesss = new ArrayList<>();
    }

    public aadl2_SubprogramGroupType(
        ArrayList<aadl2_SubprogramGroupAccess> aadl2_subprogramgroupaccesss,        ArrayList<aadl2_SubprogramAccess> aadl2_subprogramaccesss    ) {
        this.aadl2_subprogramgroupaccesss = aadl2_subprogramgroupaccesss;
        this.aadl2_subprogramaccesss = aadl2_subprogramaccesss;
    }


    public List<aadl2_SubprogramGroupAccess> getAadl2_subprogramgroupaccesss() {
        return aadl2_subprogramgroupaccesss;
    }

    public void addAadl2_subprogramgroupaccess(Aadl2_subprogramgroupaccess aadl2_subprogramgroupaccess) {
        this.aadl2_subprogramgroupaccesss.add(aadl2_subprogramgroupaccess);
    }
    public List<aadl2_SubprogramAccess> getAadl2_subprogramaccesss() {
        return aadl2_subprogramaccesss;
    }

    public void addAadl2_subprogramaccess(Aadl2_subprogramaccess aadl2_subprogramaccess) {
        this.aadl2_subprogramaccesss.add(aadl2_subprogramaccess);
    }

}