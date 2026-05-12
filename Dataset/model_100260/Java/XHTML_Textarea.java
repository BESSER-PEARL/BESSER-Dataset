





import java.util.List;
import java.util.ArrayList;

public class XHTML_Textarea extends Focus, Attrs, PCDATA, Inlineforms {

    private String readonly;
    private String disabled;





    private CDATA cdata;




    private ScriptExpression scriptexpression;




    private ScriptExpression scriptexpression;


    public XHTML_Textarea(
        String readonly,        String disabled    ) {
        super(
        );
        this.readonly = readonly;
        this.disabled = disabled;
    }


    public String getReadonly() {
        return readonly;
    }

    public void setReadonly(String readonly) {
        this.readonly = readonly;
    }
    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }

    public CDATA getCdata() {
        return cdata;
    }

    public void setCdata(CDATA cdata) {
        this.cdata = cdata;
    }
    public ScriptExpression getScriptexpression() {
        return scriptexpression;
    }

    public void setScriptexpression(ScriptExpression scriptexpression) {
        this.scriptexpression = scriptexpression;
    }
    public ScriptExpression getScriptexpression() {
        return scriptexpression;
    }

    public void setScriptexpression(ScriptExpression scriptexpression) {
        this.scriptexpression = scriptexpression;
    }

}