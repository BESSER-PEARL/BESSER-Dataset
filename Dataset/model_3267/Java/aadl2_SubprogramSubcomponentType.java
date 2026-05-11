





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramSubcomponentType extends FeatureClassifier, SubcomponentType {






    private aadl2_SubprogramSubcomponent aadl2_subprogramsubcomponent;




    private aadl2_SubprogramAccess aadl2_subprogramaccess;


    public aadl2_SubprogramSubcomponentType(
    ) {
        super(
        );
    }



    public aadl2_SubprogramSubcomponent getAadl2_subprogramsubcomponent() {
        return aadl2_subprogramsubcomponent;
    }

    public void setAadl2_subprogramsubcomponent(aadl2_SubprogramSubcomponent aadl2_subprogramsubcomponent) {
        this.aadl2_subprogramsubcomponent = aadl2_subprogramsubcomponent;
    }
    public aadl2_SubprogramAccess getAadl2_subprogramaccess() {
        return aadl2_subprogramaccess;
    }

    public void setAadl2_subprogramaccess(aadl2_SubprogramAccess aadl2_subprogramaccess) {
        this.aadl2_subprogramaccess = aadl2_subprogramaccess;
    }

}