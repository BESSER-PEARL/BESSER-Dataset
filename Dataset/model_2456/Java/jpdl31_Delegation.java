





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Delegation  {

    private String configType;
    private String mixed;
    private String class_;
    private String any;





    private jpdl31_DecisionType jpdl31_decisiontype;


    public jpdl31_Delegation(
        String configType,        String mixed,        String class_,        String any    ) {
        this.configType = configType;
        this.mixed = mixed;
        this.class_ = class_;
        this.any = any;
    }


    public String getConfigtype() {
        return configType;
    }

    public void setConfigtype(String configType) {
        this.configType = configType;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
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

    public jpdl31_DecisionType getJpdl31_decisiontype() {
        return jpdl31_decisiontype;
    }

    public void setJpdl31_decisiontype(jpdl31_DecisionType jpdl31_decisiontype) {
        this.jpdl31_decisiontype = jpdl31_decisiontype;
    }

}