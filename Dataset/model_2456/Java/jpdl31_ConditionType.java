





import java.util.List;
import java.util.ArrayList;

public class jpdl31_ConditionType  {

    private String group;
    private String any;
    private String expression;
    private String mixed;



    public jpdl31_ConditionType(
        String group,        String any,        String expression,        String mixed    ) {
        this.group = group;
        this.any = any;
        this.expression = expression;
        this.mixed = mixed;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }


}