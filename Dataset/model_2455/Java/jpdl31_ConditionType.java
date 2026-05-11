





import java.util.List;
import java.util.ArrayList;

public class jpdl31_ConditionType  {

    private String any;
    private String mixed;
    private String group;
    private String expression;



    public jpdl31_ConditionType(
        String any,        String mixed,        String group,        String expression    ) {
        this.any = any;
        this.mixed = mixed;
        this.group = group;
        this.expression = expression;
    }


    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}