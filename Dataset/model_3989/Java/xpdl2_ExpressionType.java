





import java.util.List;
import java.util.ArrayList;

public class xpdl2_ExpressionType  {

    private String scriptType;
    private String group;
    private String any;
    private String scriptVersion;
    private String mixed;
    private String scriptGrammar;



    public xpdl2_ExpressionType(
        String scriptType,        String group,        String any,        String scriptVersion,        String mixed,        String scriptGrammar    ) {
        this.scriptType = scriptType;
        this.group = group;
        this.any = any;
        this.scriptVersion = scriptVersion;
        this.mixed = mixed;
        this.scriptGrammar = scriptGrammar;
    }


    public String getScripttype() {
        return scriptType;
    }

    public void setScripttype(String scriptType) {
        this.scriptType = scriptType;
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
    public String getScriptversion() {
        return scriptVersion;
    }

    public void setScriptversion(String scriptVersion) {
        this.scriptVersion = scriptVersion;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getScriptgrammar() {
        return scriptGrammar;
    }

    public void setScriptgrammar(String scriptGrammar) {
        this.scriptGrammar = scriptGrammar;
    }


}