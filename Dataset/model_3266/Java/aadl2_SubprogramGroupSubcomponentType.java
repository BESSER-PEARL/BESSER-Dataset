





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramGroupSubcomponentType extends SubcomponentType, AbstractFeatureClassifier {






    private aadl2_SubprogramGroupAccess aadl2_subprogramgroupaccess;




    private aadl2_SubprogramGroupSubcomponent aadl2_subprogramgroupsubcomponent;


    public aadl2_SubprogramGroupSubcomponentType(
    ) {
        super(
        );
    }



    public aadl2_SubprogramGroupAccess getAadl2_subprogramgroupaccess() {
        return aadl2_subprogramgroupaccess;
    }

    public void setAadl2_subprogramgroupaccess(aadl2_SubprogramGroupAccess aadl2_subprogramgroupaccess) {
        this.aadl2_subprogramgroupaccess = aadl2_subprogramgroupaccess;
    }
    public aadl2_SubprogramGroupSubcomponent getAadl2_subprogramgroupsubcomponent() {
        return aadl2_subprogramgroupsubcomponent;
    }

    public void setAadl2_subprogramgroupsubcomponent(aadl2_SubprogramGroupSubcomponent aadl2_subprogramgroupsubcomponent) {
        this.aadl2_subprogramgroupsubcomponent = aadl2_subprogramgroupsubcomponent;
    }

}