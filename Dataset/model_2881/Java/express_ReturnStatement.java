





import java.util.List;
import java.util.ArrayList;

public class express_ReturnStatement extends Statement {

    private String expression;



    public express_ReturnStatement(
        String expression    ) {
        super(
        );
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}