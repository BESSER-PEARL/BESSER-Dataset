





import java.util.List;
import java.util.ArrayList;

public class jpdl32_ConditionType  {

    private String expression;
    private String group;
    private String any;
    private String mixed;



    public jpdl32_ConditionType(
        String expression,        String group,        String any,        String mixed    ) {
        this.expression = expression;
        this.group = group;
        this.any = any;
        this.mixed = mixed;
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


}