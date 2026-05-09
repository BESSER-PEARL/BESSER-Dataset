





import java.util.List;
import java.util.ArrayList;

public class uml_TimeEvent extends Event {

    private String isRelative;





    private uml_TimeExpression uml_timeexpression;


    public uml_TimeEvent(
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

    public uml_TimeExpression getUml_timeexpression() {
        return uml_timeexpression;
    }

    public void setUml_timeexpression(uml_TimeExpression uml_timeexpression) {
        this.uml_timeexpression = uml_timeexpression;
    }

}