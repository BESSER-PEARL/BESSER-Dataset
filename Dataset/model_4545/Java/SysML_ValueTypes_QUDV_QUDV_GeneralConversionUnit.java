





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit extends ConversionBasedUnit {

    private String expressionLanguageURI;
    private String expression;



    public SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit(
        String expressionLanguageURI,        String expression    ) {
        super(
        );
        this.expressionLanguageURI = expressionLanguageURI;
        this.expression = expression;
    }


    public String getExpressionlanguageuri() {
        return expressionLanguageURI;
    }

    public void setExpressionlanguageuri(String expressionLanguageURI) {
        this.expressionLanguageURI = expressionLanguageURI;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}