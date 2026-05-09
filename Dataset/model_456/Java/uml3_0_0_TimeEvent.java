





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_TimeEvent extends Event {

    private String isRelative;





    private uml3_0_0_TimeExpression uml3_0_0_timeexpression;


    public uml3_0_0_TimeEvent(
        String isRelative    ) {
        super(
        );
        this.isRelative = isRelative;
    }


    public String getIsrelative() {
        return isRelative;
    }

    public void setIsrelative(String isRelative) {
        this.isRelative = isRelative;
    }

    public uml3_0_0_TimeExpression getUml3_0_0_timeexpression() {
        return uml3_0_0_timeexpression;
    }

    public void setUml3_0_0_timeexpression(uml3_0_0_TimeExpression uml3_0_0_timeexpression) {
        this.uml3_0_0_timeexpression = uml3_0_0_timeexpression;
    }

}