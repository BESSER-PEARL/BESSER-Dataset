





import java.util.List;
import java.util.ArrayList;

public class xpdl2_LoopStandardType  {

    private String loopMaximum;
    private String testTime;





    private xpdl2_ExpressionType xpdl2_expressiontype;


    public xpdl2_LoopStandardType(
        String loopMaximum,        String testTime    ) {
        this.loopMaximum = loopMaximum;
        this.testTime = testTime;
    }


    public String getLoopmaximum() {
        return loopMaximum;
    }

    public void setLoopmaximum(String loopMaximum) {
        this.loopMaximum = loopMaximum;
    }
    public String getTesttime() {
        return testTime;
    }

    public void setTesttime(String testTime) {
        this.testTime = testTime;
    }

    public xpdl2_ExpressionType getXpdl2_expressiontype() {
        return xpdl2_expressiontype;
    }

    public void setXpdl2_expressiontype(xpdl2_ExpressionType xpdl2_expressiontype) {
        this.xpdl2_expressiontype = xpdl2_expressiontype;
    }

}