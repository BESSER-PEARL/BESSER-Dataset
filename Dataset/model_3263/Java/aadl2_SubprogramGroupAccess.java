





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramGroupAccess extends CallContext, Access, SubprogramGroup {






    private aadl2_SubprogramGroupSubcomponentType aadl2_subprogramgroupsubcomponenttype;




    private aadl2_DataType aadl2_datatype;




    private aadl2_SubprogramGroupType aadl2_subprogramgrouptype;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;


    public aadl2_SubprogramGroupAccess(
    ) {
        super(
        );
    }



    public aadl2_SubprogramGroupSubcomponentType getAadl2_subprogramgroupsubcomponenttype() {
        return aadl2_subprogramgroupsubcomponenttype;
    }

    public void setAadl2_subprogramgroupsubcomponenttype(aadl2_SubprogramGroupSubcomponentType aadl2_subprogramgroupsubcomponenttype) {
        this.aadl2_subprogramgroupsubcomponenttype = aadl2_subprogramgroupsubcomponenttype;
    }
    public aadl2_DataType getAadl2_datatype() {
        return aadl2_datatype;
    }

    public void setAadl2_datatype(aadl2_DataType aadl2_datatype) {
        this.aadl2_datatype = aadl2_datatype;
    }
    public aadl2_SubprogramGroupType getAadl2_subprogramgrouptype() {
        return aadl2_subprogramgrouptype;
    }

    public void setAadl2_subprogramgrouptype(aadl2_SubprogramGroupType aadl2_subprogramgrouptype) {
        this.aadl2_subprogramgrouptype = aadl2_subprogramgrouptype;
    }
    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }

}