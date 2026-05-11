





import java.util.List;
import java.util.ArrayList;

public class model_Expression extends ExtensibilityElement {

    private String expressionLanguage;
    private String body;
    private String opaque;





    private model_OnAlarm model_onalarm;




    private model_OnAlarm model_onalarm;




    private model_Wait model_wait;




    private model_ForEach model_foreach;




    private model_ForEach model_foreach;




    private model_OnAlarm model_onalarm;




    private model_Wait model_wait;


    public model_Expression(
        String expressionLanguage,        String body,        String opaque    ) {
        super(
        );
        this.expressionLanguage = expressionLanguage;
        this.body = body;
        this.opaque = opaque;
    }


    public String getExpressionlanguage() {
        return expressionLanguage;
    }

    public void setExpressionlanguage(String expressionLanguage) {
        this.expressionLanguage = expressionLanguage;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getOpaque() {
        return opaque;
    }

    public void setOpaque(String opaque) {
        this.opaque = opaque;
    }

    public model_OnAlarm getModel_onalarm() {
        return model_onalarm;
    }

    public void setModel_onalarm(model_OnAlarm model_onalarm) {
        this.model_onalarm = model_onalarm;
    }
    public model_OnAlarm getModel_onalarm() {
        return model_onalarm;
    }

    public void setModel_onalarm(model_OnAlarm model_onalarm) {
        this.model_onalarm = model_onalarm;
    }
    public model_Wait getModel_wait() {
        return model_wait;
    }

    public void setModel_wait(model_Wait model_wait) {
        this.model_wait = model_wait;
    }
    public model_ForEach getModel_foreach() {
        return model_foreach;
    }

    public void setModel_foreach(model_ForEach model_foreach) {
        this.model_foreach = model_foreach;
    }
    public model_ForEach getModel_foreach() {
        return model_foreach;
    }

    public void setModel_foreach(model_ForEach model_foreach) {
        this.model_foreach = model_foreach;
    }
    public model_OnAlarm getModel_onalarm() {
        return model_onalarm;
    }

    public void setModel_onalarm(model_OnAlarm model_onalarm) {
        this.model_onalarm = model_onalarm;
    }
    public model_Wait getModel_wait() {
        return model_wait;
    }

    public void setModel_wait(model_Wait model_wait) {
        this.model_wait = model_wait;
    }

}