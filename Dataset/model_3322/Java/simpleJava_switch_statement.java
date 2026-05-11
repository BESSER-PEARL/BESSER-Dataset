





import java.util.List;
import java.util.ArrayList;

public class simpleJava_switch_statement  {






    private simpleJava_statement simplejava_statement;




    private List<simpleJava_expression> simplejava_expressions;




    private simpleJava_statement simplejava_statement;




    private simpleJava_expression simplejava_expression;


    public simpleJava_switch_statement(
    ) {
        this.simplejava_expressions = new ArrayList<>();
    }

    public simpleJava_switch_statement(
        ArrayList<simpleJava_expression> simplejava_expressions    ) {
        this.simplejava_expressions = simplejava_expressions;
    }


    public simpleJava_statement getSimplejava_statement() {
        return simplejava_statement;
    }

    public void setSimplejava_statement(simpleJava_statement simplejava_statement) {
        this.simplejava_statement = simplejava_statement;
    }
    public List<simpleJava_expression> getSimplejava_expressions() {
        return simplejava_expressions;
    }

    public void addSimplejava_expression(Simplejava_expression simplejava_expression) {
        this.simplejava_expressions.add(simplejava_expression);
    }
    public simpleJava_statement getSimplejava_statement() {
        return simplejava_statement;
    }

    public void setSimplejava_statement(simpleJava_statement simplejava_statement) {
        this.simplejava_statement = simplejava_statement;
    }
    public simpleJava_expression getSimplejava_expression() {
        return simplejava_expression;
    }

    public void setSimplejava_expression(simpleJava_expression simplejava_expression) {
        this.simplejava_expression = simplejava_expression;
    }

}