





import java.util.List;
import java.util.ArrayList;

public class smif_expressions_ExpressionNode extends ExpressionContext {

    private String expressionTextLanguage;
    private String expressionText;



    public smif_expressions_ExpressionNode(
        String expressionTextLanguage,        String expressionText    ) {
        super(
        );
        this.expressionTextLanguage = expressionTextLanguage;
        this.expressionText = expressionText;
    }


    public String getExpressiontextlanguage() {
        return expressionTextLanguage;
    }

    public void setExpressiontextlanguage(String expressionTextLanguage) {
        this.expressionTextLanguage = expressionTextLanguage;
    }
    public String getExpressiontext() {
        return expressionText;
    }

    public void setExpressiontext(String expressionText) {
        this.expressionText = expressionText;
    }


}