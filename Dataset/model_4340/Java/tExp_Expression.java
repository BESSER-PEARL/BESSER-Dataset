





import java.util.List;
import java.util.ArrayList;

public class tExp_Expression  {

    private String operator;
    private String eps;
    private String variable;





    private List<tExp_PrologExpression> texp_prologexpressions;




    private tExp_EventType texp_eventtype;




    private tExp_Expression texp_expression;




    private tExp_Term texp_term;




    private tExp_Expression texp_expression;




    private tExp_Term texp_term;




    private tExp_PrologExpression texp_prologexpression;




    private tExp_Expression texp_expression;




    private tExp_Expression texp_expression;




    private tExp_EventType texp_eventtype;


    public tExp_Expression(
        String operator,        String eps,        String variable    ) {
        this.operator = operator;
        this.eps = eps;
        this.variable = variable;
        this.texp_prologexpressions = new ArrayList<>();
    }

    public tExp_Expression(
        String operator,        String eps,        String variable        ArrayList<tExp_PrologExpression> texp_prologexpressions    ) {
        this.operator = operator;
        this.eps = eps;
        this.variable = variable;
        this.texp_prologexpressions = texp_prologexpressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getEps() {
        return eps;
    }

    public void setEps(String eps) {
        this.eps = eps;
    }
    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public List<tExp_PrologExpression> getTexp_prologexpressions() {
        return texp_prologexpressions;
    }

    public void addTexp_prologexpression(Texp_prologexpression texp_prologexpression) {
        this.texp_prologexpressions.add(texp_prologexpression);
    }
    public tExp_EventType getTexp_eventtype() {
        return texp_eventtype;
    }

    public void setTexp_eventtype(tExp_EventType texp_eventtype) {
        this.texp_eventtype = texp_eventtype;
    }
    public tExp_Expression getTexp_expression() {
        return texp_expression;
    }

    public void setTexp_expression(tExp_Expression texp_expression) {
        this.texp_expression = texp_expression;
    }
    public tExp_Term getTexp_term() {
        return texp_term;
    }

    public void setTexp_term(tExp_Term texp_term) {
        this.texp_term = texp_term;
    }
    public tExp_Expression getTexp_expression() {
        return texp_expression;
    }

    public void setTexp_expression(tExp_Expression texp_expression) {
        this.texp_expression = texp_expression;
    }
    public tExp_Term getTexp_term() {
        return texp_term;
    }

    public void setTexp_term(tExp_Term texp_term) {
        this.texp_term = texp_term;
    }
    public tExp_PrologExpression getTexp_prologexpression() {
        return texp_prologexpression;
    }

    public void setTexp_prologexpression(tExp_PrologExpression texp_prologexpression) {
        this.texp_prologexpression = texp_prologexpression;
    }
    public tExp_Expression getTexp_expression() {
        return texp_expression;
    }

    public void setTexp_expression(tExp_Expression texp_expression) {
        this.texp_expression = texp_expression;
    }
    public tExp_Expression getTexp_expression() {
        return texp_expression;
    }

    public void setTexp_expression(tExp_Expression texp_expression) {
        this.texp_expression = texp_expression;
    }
    public tExp_EventType getTexp_eventtype() {
        return texp_eventtype;
    }

    public void setTexp_eventtype(tExp_EventType texp_eventtype) {
        this.texp_eventtype = texp_eventtype;
    }

}