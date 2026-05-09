





import java.util.List;
import java.util.ArrayList;

public class mMDSL_AttributeGet  {

    private String attrgetparams;





    private mMDSL_AttributeOperation mmdsl_attributeoperation;


    public mMDSL_AttributeGet(
        String attrgetparams    ) {
        this.attrgetparams = attrgetparams;
    }


    public String getAttrgetparams() {
        return attrgetparams;
    }

    public void setAttrgetparams(String attrgetparams) {
        this.attrgetparams = attrgetparams;
    }

    public mMDSL_AttributeOperation getMmdsl_attributeoperation() {
        return mmdsl_attributeoperation;
    }

    public void setMmdsl_attributeoperation(mMDSL_AttributeOperation mmdsl_attributeoperation) {
        this.mmdsl_attributeoperation = mmdsl_attributeoperation;
    }

}