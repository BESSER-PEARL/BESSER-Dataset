





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_ScriptExpression extends Expression {

    private String script;





    private scxmlxt_EStepFilter scxmlxt_estepfilter;


    public scxmlxt_ScriptExpression(
        String script    ) {
        super(
        );
        this.script = script;
    }


    public String getScript() {
        return script;
    }

    public void setScript(String script) {
        this.script = script;
    }

    public scxmlxt_EStepFilter getScxmlxt_estepfilter() {
        return scxmlxt_estepfilter;
    }

    public void setScxmlxt_estepfilter(scxmlxt_EStepFilter scxmlxt_estepfilter) {
        this.scxmlxt_estepfilter = scxmlxt_estepfilter;
    }

}