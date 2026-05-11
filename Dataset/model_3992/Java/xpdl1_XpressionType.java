





import java.util.List;
import java.util.ArrayList;

public class xpdl1_XpressionType  {

    private String group;
    private String mixed;
    private String any;





    private xpdl1_ConditionType xpdl1_conditiontype;


    public xpdl1_XpressionType(
        String group,        String mixed,        String any    ) {
        this.group = group;
        this.mixed = mixed;
        this.any = any;
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

    public xpdl1_ConditionType getXpdl1_conditiontype() {
        return xpdl1_conditiontype;
    }

    public void setXpdl1_conditiontype(xpdl1_ConditionType xpdl1_conditiontype) {
        this.xpdl1_conditiontype = xpdl1_conditiontype;
    }

}