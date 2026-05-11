





import java.util.List;
import java.util.ArrayList;

public class nuSMV_UnaryRTCTLExpression extends RTCTLExpression {

    private String unary;





    private nuSMV_RTCTLExpression nusmv_rtctlexpression;




    private nuSMV_RangeExpression nusmv_rangeexpression;


    public nuSMV_UnaryRTCTLExpression(
        String unary    ) {
        super(
        );
        this.unary = unary;
    }


    public String getUnary() {
        return unary;
    }

    public void setUnary(String unary) {
        this.unary = unary;
    }

    public nuSMV_RTCTLExpression getNusmv_rtctlexpression() {
        return nusmv_rtctlexpression;
    }

    public void setNusmv_rtctlexpression(nuSMV_RTCTLExpression nusmv_rtctlexpression) {
        this.nusmv_rtctlexpression = nusmv_rtctlexpression;
    }
    public nuSMV_RangeExpression getNusmv_rangeexpression() {
        return nusmv_rangeexpression;
    }

    public void setNusmv_rangeexpression(nuSMV_RangeExpression nusmv_rangeexpression) {
        this.nusmv_rangeexpression = nusmv_rangeexpression;
    }

}