





import java.util.List;
import java.util.ArrayList;

public class aadl2_BusAccess extends Access {

    private String virtual;





    private aadl2_AbstractType aadl2_abstracttype;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;


    public aadl2_BusAccess(
        String virtual    ) {
        super(
        );
        this.virtual = virtual;
    }


    public String getVirtual() {
        return virtual;
    }

    public void setVirtual(String virtual) {
        this.virtual = virtual;
    }

    public aadl2_AbstractType getAadl2_abstracttype() {
        return aadl2_abstracttype;
    }

    public void setAadl2_abstracttype(aadl2_AbstractType aadl2_abstracttype) {
        this.aadl2_abstracttype = aadl2_abstracttype;
    }
    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }

}