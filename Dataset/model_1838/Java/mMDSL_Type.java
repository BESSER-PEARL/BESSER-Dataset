





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Type  {

    private String simpletype;





    private mMDSL_ClassAttribute mmdsl_classattribute;




    private mMDSL_Attribute mmdsl_attribute;


    public mMDSL_Type(
        String simpletype    ) {
        this.simpletype = simpletype;
    }


    public String getSimpletype() {
        return simpletype;
    }

    public void setSimpletype(String simpletype) {
        this.simpletype = simpletype;
    }

    public mMDSL_ClassAttribute getMmdsl_classattribute() {
        return mmdsl_classattribute;
    }

    public void setMmdsl_classattribute(mMDSL_ClassAttribute mmdsl_classattribute) {
        this.mmdsl_classattribute = mmdsl_classattribute;
    }
    public mMDSL_Attribute getMmdsl_attribute() {
        return mmdsl_attribute;
    }

    public void setMmdsl_attribute(mMDSL_Attribute mmdsl_attribute) {
        this.mmdsl_attribute = mmdsl_attribute;
    }

}