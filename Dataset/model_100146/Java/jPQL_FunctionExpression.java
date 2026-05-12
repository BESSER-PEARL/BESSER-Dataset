





import java.util.List;
import java.util.ArrayList;

public class jPQL_FunctionExpression extends Expression {

    private String name;
    private String trimSpec;





    private jPQL_Expression jpql_expression;




    private List<jPQL_Expression> jpql_expressions;




    private jPQL_Expression jpql_expression;




    private jPQL_Expression jpql_expression;




    private jPQL_Expression jpql_expression;


    public jPQL_FunctionExpression(
        String name,        String trimSpec    ) {
        super(
        );
        this.name = name;
        this.trimSpec = trimSpec;
        this.jpql_expressions = new ArrayList<>();
    }

    public jPQL_FunctionExpression(
        String name,        String trimSpec        ArrayList<jPQL_Expression> jpql_expressions    ) {
        this.name = name;
        this.trimSpec = trimSpec;
        this.jpql_expressions = jpql_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTrimspec() {
        return trimSpec;
    }

    public void setTrimspec(String trimSpec) {
        this.trimSpec = trimSpec;
    }

    public jPQL_Expression getJpql_expression() {
        return jpql_expression;
    }

    public void setJpql_expression(jPQL_Expression jpql_expression) {
        this.jpql_expression = jpql_expression;
    }
    public List<jPQL_Expression> getJpql_expressions() {
        return jpql_expressions;
    }

    public void addJpql_expression(Jpql_expression jpql_expression) {
        this.jpql_expressions.add(jpql_expression);
    }
    public jPQL_Expression getJpql_expression() {
        return jpql_expression;
    }

    public void setJpql_expression(jPQL_Expression jpql_expression) {
        this.jpql_expression = jpql_expression;
    }
    public jPQL_Expression getJpql_expression() {
        return jpql_expression;
    }

    public void setJpql_expression(jPQL_Expression jpql_expression) {
        this.jpql_expression = jpql_expression;
    }
    public jPQL_Expression getJpql_expression() {
        return jpql_expression;
    }

    public void setJpql_expression(jPQL_Expression jpql_expression) {
        this.jpql_expression = jpql_expression;
    }

}