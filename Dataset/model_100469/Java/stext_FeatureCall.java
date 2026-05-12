





import java.util.List;
import java.util.ArrayList;

public class stext_FeatureCall extends Expression {

    private boolean operationCall;





    private List<stext_Expression> stext_expressions;




    private stext_Expression stext_expression;


    public stext_FeatureCall(
        boolean operationCall    ) {
        super(
        );
        this.operationCall = operationCall;
        this.stext_expressions = new ArrayList<>();
    }

    public stext_FeatureCall(
        boolean operationCall        ArrayList<stext_Expression> stext_expressions    ) {
        this.operationCall = operationCall;
        this.stext_expressions = stext_expressions;
    }

    public boolean getOperationcall() {
        return operationCall;
    }

    public void setOperationcall(boolean operationCall) {
        this.operationCall = operationCall;
    }

    public List<stext_Expression> getStext_expressions() {
        return stext_expressions;
    }

    public void addStext_expression(Stext_expression stext_expression) {
        this.stext_expressions.add(stext_expression);
    }
    public stext_Expression getStext_expression() {
        return stext_expression;
    }

    public void setStext_expression(stext_Expression stext_expression) {
        this.stext_expression = stext_expression;
    }

}