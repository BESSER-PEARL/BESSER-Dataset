





import java.util.List;
import java.util.ArrayList;

public class aadl2_BusAccess extends Bus, Access {






    private aadl2_AbstractType aadl2_abstracttype;




    private aadl2_BusSubcomponentType aadl2_bussubcomponenttype;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;


    public aadl2_BusAccess(
    ) {
        super(
        );
    }



    public aadl2_AbstractType getAadl2_abstracttype() {
        return aadl2_abstracttype;
    }

    public void setAadl2_abstracttype(aadl2_AbstractType aadl2_abstracttype) {
        this.aadl2_abstracttype = aadl2_abstracttype;
    }
    public aadl2_BusSubcomponentType getAadl2_bussubcomponenttype() {
        return aadl2_bussubcomponenttype;
    }

    public void setAadl2_bussubcomponenttype(aadl2_BusSubcomponentType aadl2_bussubcomponenttype) {
        this.aadl2_bussubcomponenttype = aadl2_bussubcomponenttype;
    }
    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }

}