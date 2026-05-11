





import java.util.List;
import java.util.ArrayList;

public class aadl2_AbstractFeature extends DirectedFeature, TriggerPort {






    private aadl2_FeatureGroupType aadl2_featuregrouptype;




    private aadl2_ComponentType aadl2_componenttype;


    public aadl2_AbstractFeature(
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
    public aadl2_ComponentType getAadl2_componenttype() {
        return aadl2_componenttype;
    }

    public void setAadl2_componenttype(aadl2_ComponentType aadl2_componenttype) {
        this.aadl2_componenttype = aadl2_componenttype;
    }

}