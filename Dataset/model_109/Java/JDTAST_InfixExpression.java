





import java.util.List;
import java.util.ArrayList;

public class JDTAST_InfixExpression extends Expression {

    private String operator;





    private List<JDTAST_Expression> jdtast_expressions;




    private JDTAST_Expression jdtast_expression;




    private JDTAST_Expression jdtast_expression;


    public JDTAST_InfixExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.jdtast_expressions = new ArrayList<>();
    }

    public JDTAST_InfixExpression(
        String operator        ArrayList<JDTAST_Expression> jdtast_expressions    ) {
        this.operator = operator;
        this.jdtast_expressions = jdtast_expressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<JDTAST_Expression> getJdtast_expressions() {
        return jdtast_expressions;
    }

    public void addJdtast_expression(Jdtast_expression jdtast_expression) {
        this.jdtast_expressions.add(jdtast_expression);
    }
    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }
    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }

}