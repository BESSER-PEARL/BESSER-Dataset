





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit extends ConversionBasedUnit {

    private String expression;
    private String expressionLanguageURI;



    public SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit(
        String expression,        String expressionLanguageURI    ) {
        super(
        );
        this.expression = expression;
        this.expressionLanguageURI = expressionLanguageURI;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getExpressionlanguageuri() {
        return expressionLanguageURI;
    }

    public void setExpressionlanguageuri(String expressionLanguageURI) {
        this.expressionLanguageURI = expressionLanguageURI;
    }


}