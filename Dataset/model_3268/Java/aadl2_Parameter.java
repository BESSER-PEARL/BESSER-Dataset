





import java.util.List;
import java.util.ArrayList;

public class aadl2_Parameter extends Context, DirectedFeature, ParameterConnectionEnd {






    private aadl2_FeatureGroupType aadl2_featuregrouptype;




    private aadl2_SubprogramType aadl2_subprogramtype;




    private aadl2_DataSubcomponentType aadl2_datasubcomponenttype;


    public aadl2_Parameter(
    ) {
        super(
        );
    }



    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }
    public aadl2_SubprogramType getAadl2_subprogramtype() {
        return aadl2_subprogramtype;
    }

    public void setAadl2_subprogramtype(aadl2_SubprogramType aadl2_subprogramtype) {
        this.aadl2_subprogramtype = aadl2_subprogramtype;
    }
    public aadl2_DataSubcomponentType getAadl2_datasubcomponenttype() {
        return aadl2_datasubcomponenttype;
    }

    public void setAadl2_datasubcomponenttype(aadl2_DataSubcomponentType aadl2_datasubcomponenttype) {
        this.aadl2_datasubcomponenttype = aadl2_datasubcomponenttype;
    }

}