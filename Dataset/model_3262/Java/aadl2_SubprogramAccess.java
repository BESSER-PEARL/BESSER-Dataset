





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramAccess extends Access, Subprogram {






    private aadl2_AbstractType aadl2_abstracttype;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;




    private aadl2_SubprogramGroupType aadl2_subprogramgrouptype;




    private aadl2_SubprogramType aadl2_subprogramtype;




    private aadl2_SubprogramSubcomponentType aadl2_subprogramsubcomponenttype;




    private aadl2_DataType aadl2_datatype;


    public aadl2_SubprogramAccess(
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
    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }
    public aadl2_SubprogramGroupType getAadl2_subprogramgrouptype() {
        return aadl2_subprogramgrouptype;
    }

    public void setAadl2_subprogramgrouptype(aadl2_SubprogramGroupType aadl2_subprogramgrouptype) {
        this.aadl2_subprogramgrouptype = aadl2_subprogramgrouptype;
    }
    public aadl2_SubprogramType getAadl2_subprogramtype() {
        return aadl2_subprogramtype;
    }

    public void setAadl2_subprogramtype(aadl2_SubprogramType aadl2_subprogramtype) {
        this.aadl2_subprogramtype = aadl2_subprogramtype;
    }
    public aadl2_SubprogramSubcomponentType getAadl2_subprogramsubcomponenttype() {
        return aadl2_subprogramsubcomponenttype;
    }

    public void setAadl2_subprogramsubcomponenttype(aadl2_SubprogramSubcomponentType aadl2_subprogramsubcomponenttype) {
        this.aadl2_subprogramsubcomponenttype = aadl2_subprogramsubcomponenttype;
    }
    public aadl2_DataType getAadl2_datatype() {
        return aadl2_datatype;
    }

    public void setAadl2_datatype(aadl2_DataType aadl2_datatype) {
        this.aadl2_datatype = aadl2_datatype;
    }

}