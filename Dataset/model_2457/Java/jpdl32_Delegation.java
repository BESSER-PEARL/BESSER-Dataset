





import java.util.List;
import java.util.ArrayList;

public class jpdl32_Delegation  {

    private String mixed;
    private String configType;
    private String class_;
    private String any;





    private jpdl32_DecisionType jpdl32_decisiontype;


    public jpdl32_Delegation(
        String mixed,        String configType,        String class_,        String any    ) {
        this.mixed = mixed;
        this.configType = configType;
        this.class_ = class_;
        this.any = any;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
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

    public jpdl32_DecisionType getJpdl32_decisiontype() {
        return jpdl32_decisiontype;
    }

    public void setJpdl32_decisiontype(jpdl32_DecisionType jpdl32_decisiontype) {
        this.jpdl32_decisiontype = jpdl32_decisiontype;
    }

}