





import java.util.List;
import java.util.ArrayList;

public class jpdl32_ConditionType  {

    private String expression;
    private String group;
    private String mixed;
    private String any;



    public jpdl32_ConditionType(
        String expression,        String group,        String mixed,        String any    ) {
        this.expression = expression;
        this.group = group;
        this.mixed = mixed;
        this.any = any;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }


}