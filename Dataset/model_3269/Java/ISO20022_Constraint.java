





import java.util.List;
import java.util.ArrayList;

public class ISO20022_Constraint  {

    private String expressionLanguage;
    private boolean injected;
    private String kind;
    private String errorText;
    private String errorCode;
    private String expression;



    public ISO20022_Constraint(
        String expressionLanguage,        boolean injected,        String kind,        String errorText,        String errorCode,        String expression    ) {
        this.expressionLanguage = expressionLanguage;
        this.injected = injected;
        this.kind = kind;
        this.errorText = errorText;
        this.errorCode = errorCode;
        this.expression = expression;
    }


    public String getExpressionlanguage() {
        return expressionLanguage;
    }

    public void setExpressionlanguage(String expressionLanguage) {
        this.expressionLanguage = expressionLanguage;
    }
    public boolean getInjected() {
        return injected;
    }

    public void setInjected(boolean injected) {
        this.injected = injected;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getErrortext() {
        return errorText;
    }

    public void setErrortext(String errorText) {
        this.errorText = errorText;
    }
    public String getErrorcode() {
        return errorCode;
    }

    public void setErrorcode(String errorCode) {
        this.errorCode = errorCode;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}