





import java.util.List;
import java.util.ArrayList;

public class mprologTermReference_Operator  {

    private String symbol;





    private mprologTermReference_InfixExpression mprologtermreference_infixexpression;


    public mprologTermReference_Operator(
        String symbol    ) {
        this.symbol = symbol;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public mprologTermReference_InfixExpression getMprologtermreference_infixexpression() {
        return mprologtermreference_infixexpression;
    }

    public void setMprologtermreference_infixexpression(mprologTermReference_InfixExpression mprologtermreference_infixexpression) {
        this.mprologtermreference_infixexpression = mprologtermreference_infixexpression;
    }

}