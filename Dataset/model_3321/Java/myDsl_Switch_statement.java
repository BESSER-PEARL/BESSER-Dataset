





import java.util.List;
import java.util.ArrayList;

public class myDsl_Switch_statement  {

    private String rparent;
    private String lParen;





    private List<myDsl_Statement> mydsl_statements;




    private List<myDsl_Expression> mydsl_expressions;




    private myDsl_Expression mydsl_expression;




    private myDsl_Statement mydsl_statement;


    public myDsl_Switch_statement(
        String rparent,        String lParen    ) {
        this.rparent = rparent;
        this.lParen = lParen;
        this.mydsl_statements = new ArrayList<>();
        this.mydsl_expressions = new ArrayList<>();
    }

    public myDsl_Switch_statement(
        String rparent,        String lParen        ArrayList<myDsl_Statement> mydsl_statements,        ArrayList<myDsl_Expression> mydsl_expressions    ) {
        this.rparent = rparent;
        this.lParen = lParen;
        this.mydsl_statements = mydsl_statements;
        this.mydsl_expressions = mydsl_expressions;
    }

    public String getRparent() {
        return rparent;
    }

    public void setRparent(String rparent) {
        this.rparent = rparent;
    }
    public String getLparen() {
        return lParen;
    }

    public void setLparen(String lParen) {
        this.lParen = lParen;
    }

    public List<myDsl_Statement> getMydsl_statements() {
        return mydsl_statements;
    }

    public void addMydsl_statement(Mydsl_statement mydsl_statement) {
        this.mydsl_statements.add(mydsl_statement);
    }
    public List<myDsl_Expression> getMydsl_expressions() {
        return mydsl_expressions;
    }

    public void addMydsl_expression(Mydsl_expression mydsl_expression) {
        this.mydsl_expressions.add(mydsl_expression);
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}