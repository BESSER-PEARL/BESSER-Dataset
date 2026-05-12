





import java.util.List;
import java.util.ArrayList;

public class reqSpec_DesiredValue  {

    private boolean upto;





    private reqSpec_PropertyExpression reqspec_propertyexpression;




    private reqSpec_ValuePredicate reqspec_valuepredicate;


    public reqSpec_DesiredValue(
        boolean upto    ) {
        this.upto = upto;
    }


    public boolean getUpto() {
        return upto;
    }

    public void setUpto(boolean upto) {
        this.upto = upto;
    }

    public reqSpec_PropertyExpression getReqspec_propertyexpression() {
        return reqspec_propertyexpression;
    }

    public void setReqspec_propertyexpression(reqSpec_PropertyExpression reqspec_propertyexpression) {
        this.reqspec_propertyexpression = reqspec_propertyexpression;
    }
    public reqSpec_ValuePredicate getReqspec_valuepredicate() {
        return reqspec_valuepredicate;
    }

    public void setReqspec_valuepredicate(reqSpec_ValuePredicate reqspec_valuepredicate) {
        this.reqspec_valuepredicate = reqspec_valuepredicate;
    }

}