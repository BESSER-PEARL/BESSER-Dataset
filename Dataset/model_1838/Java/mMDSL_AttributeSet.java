





import java.util.List;
import java.util.ArrayList;

public class mMDSL_AttributeSet  {

    private String valueString;
    private String attrsetparams;
    private String valueRealNumber;





    private mMDSL_AttributeOperation mmdsl_attributeoperation;




    private mMDSL_Variable mmdsl_variable;


    public mMDSL_AttributeSet(
        String valueString,        String attrsetparams,        String valueRealNumber    ) {
        this.valueString = valueString;
        this.attrsetparams = attrsetparams;
        this.valueRealNumber = valueRealNumber;
    }


    public String getValuestring() {
        return valueString;
    }

    public void setValuestring(String valueString) {
        this.valueString = valueString;
    }
    public String getAttrsetparams() {
        return attrsetparams;
    }

    public void setAttrsetparams(String attrsetparams) {
        this.attrsetparams = attrsetparams;
    }
    public String getValuerealnumber() {
        return valueRealNumber;
    }

    public void setValuerealnumber(String valueRealNumber) {
        this.valueRealNumber = valueRealNumber;
    }

    public mMDSL_AttributeOperation getMmdsl_attributeoperation() {
        return mmdsl_attributeoperation;
    }

    public void setMmdsl_attributeoperation(mMDSL_AttributeOperation mmdsl_attributeoperation) {
        this.mmdsl_attributeoperation = mmdsl_attributeoperation;
    }
    public mMDSL_Variable getMmdsl_variable() {
        return mmdsl_variable;
    }

    public void setMmdsl_variable(mMDSL_Variable mmdsl_variable) {
        this.mmdsl_variable = mmdsl_variable;
    }

}