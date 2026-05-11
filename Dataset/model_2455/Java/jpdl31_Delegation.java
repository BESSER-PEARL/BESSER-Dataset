





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Delegation  {

    private String configType;
    private String class_;
    private String any;
    private String mixed;





    private jpdl31_DecisionType jpdl31_decisiontype;


    public jpdl31_Delegation(
        String configType,        String class_,        String any,        String mixed    ) {
        this.configType = configType;
        this.class_ = class_;
        this.any = any;
        this.mixed = mixed;
    }


    public String getConfigtype() {
        return configType;
    }

    public void setConfigtype(String configType) {
        this.configType = configType;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
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

    public jpdl31_DecisionType getJpdl31_decisiontype() {
        return jpdl31_decisiontype;
    }

    public void setJpdl31_decisiontype(jpdl31_DecisionType jpdl31_decisiontype) {
        this.jpdl31_decisiontype = jpdl31_decisiontype;
    }

}