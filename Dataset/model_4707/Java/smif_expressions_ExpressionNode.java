





import java.util.List;
import java.util.ArrayList;

public class smif_expressions_ExpressionNode extends ExpressionContext {

    private String expressionText;
    private String expressionTextLanguage;



    public smif_expressions_ExpressionNode(
        String expressionText,        String expressionTextLanguage    ) {
        super(
        );
        this.expressionText = expressionText;
        this.expressionTextLanguage = expressionTextLanguage;
    }


    public String getExpressiontext() {
        return expressionText;
    }

    public void setExpressiontext(String expressionText) {
        this.expressionText = expressionText;
    }
    public String getExpressiontextlanguage() {
        return expressionTextLanguage;
    }

    public void setExpressiontextlanguage(String expressionTextLanguage) {
        this.expressionTextLanguage = expressionTextLanguage;
    }


}