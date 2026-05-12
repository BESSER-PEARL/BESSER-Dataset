





import java.util.List;
import java.util.ArrayList;

public class jPQL_Expression extends SelectExpression {

    private String unaryOperator;
    private boolean isNot;





    private List<jPQL_Variable> jpql_variables;




    private jPQL_OrExpression jpql_orexpression;




    private jPQL_AndExpression jpql_andexpression;




    private jPQL_HavingClause jpql_havingclause;




    private jPQL_Expression jpql_expression;




    private jPQL_Expression jpql_expression;




    private jPQL_WhereClause jpql_whereclause;




    private jPQL_SelectStatement jpql_selectstatement;


    public jPQL_Expression(
        String unaryOperator,        boolean isNot    ) {
        super(
        );
        this.unaryOperator = unaryOperator;
        this.isNot = isNot;
        this.jpql_variables = new ArrayList<>();
    }

    public jPQL_Expression(
        String unaryOperator,        boolean isNot        ArrayList<jPQL_Variable> jpql_variables    ) {
        this.unaryOperator = unaryOperator;
        this.isNot = isNot;
        this.jpql_variables = jpql_variables;
    }

    public String getUnaryoperator() {
        return unaryOperator;
    }

    public void setUnaryoperator(String unaryOperator) {
        this.unaryOperator = unaryOperator;
    }
    public boolean getIsnot() {
        return isNot;
    }

    public void setIsnot(boolean isNot) {
        this.isNot = isNot;
    }

    public List<jPQL_Variable> getJpql_variables() {
        return jpql_variables;
    }

    public void addJpql_variable(Jpql_variable jpql_variable) {
        this.jpql_variables.add(jpql_variable);
    }
    public jPQL_OrExpression getJpql_orexpression() {
        return jpql_orexpression;
    }

    public void setJpql_orexpression(jPQL_OrExpression jpql_orexpression) {
        this.jpql_orexpression = jpql_orexpression;
    }
    public jPQL_AndExpression getJpql_andexpression() {
        return jpql_andexpression;
    }

    public void setJpql_andexpression(jPQL_AndExpression jpql_andexpression) {
        this.jpql_andexpression = jpql_andexpression;
    }
    public jPQL_HavingClause getJpql_havingclause() {
        return jpql_havingclause;
    }

    public void setJpql_havingclause(jPQL_HavingClause jpql_havingclause) {
        this.jpql_havingclause = jpql_havingclause;
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
    public jPQL_WhereClause getJpql_whereclause() {
        return jpql_whereclause;
    }

    public void setJpql_whereclause(jPQL_WhereClause jpql_whereclause) {
        this.jpql_whereclause = jpql_whereclause;
    }
    public jPQL_SelectStatement getJpql_selectstatement() {
        return jpql_selectstatement;
    }

    public void setJpql_selectstatement(jPQL_SelectStatement jpql_selectstatement) {
        this.jpql_selectstatement = jpql_selectstatement;
    }

}