





import java.util.List;
import java.util.ArrayList;

public class myDsl_Statement  {

    private String g;
    private String name;
    private String ret;
    private String rparent;
    private String nameStatement;





    private myDsl_Statement_block mydsl_statement_block;




    private myDsl_Statement_block mydsl_statement_block;




    private myDsl_Expression mydsl_expression;




    private myDsl_Statement mydsl_statement;




    private List<myDsl_Expression> mydsl_expressions;




    private myDsl_Statement mydsl_statement;




    private myDsl_Variable_declaration mydsl_variable_declaration;


    public myDsl_Statement(
        String g,        String name,        String ret,        String rparent,        String nameStatement    ) {
        this.g = g;
        this.name = name;
        this.ret = ret;
        this.rparent = rparent;
        this.nameStatement = nameStatement;
        this.mydsl_expressions = new ArrayList<>();
    }

    public myDsl_Statement(
        String g,        String name,        String ret,        String rparent,        String nameStatement        ArrayList<myDsl_Expression> mydsl_expressions    ) {
        this.g = g;
        this.name = name;
        this.ret = ret;
        this.rparent = rparent;
        this.nameStatement = nameStatement;
        this.mydsl_expressions = mydsl_expressions;
    }

    public String getG() {
        return g;
    }

    public void setG(String g) {
        this.g = g;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRet() {
        return ret;
    }

    public void setRet(String ret) {
        this.ret = ret;
    }
    public String getRparent() {
        return rparent;
    }

    public void setRparent(String rparent) {
        this.rparent = rparent;
    }
    public String getNamestatement() {
        return nameStatement;
    }

    public void setNamestatement(String nameStatement) {
        this.nameStatement = nameStatement;
    }

    public myDsl_Statement_block getMydsl_statement_block() {
        return mydsl_statement_block;
    }

    public void setMydsl_statement_block(myDsl_Statement_block mydsl_statement_block) {
        this.mydsl_statement_block = mydsl_statement_block;
    }
    public myDsl_Statement_block getMydsl_statement_block() {
        return mydsl_statement_block;
    }

    public void setMydsl_statement_block(myDsl_Statement_block mydsl_statement_block) {
        this.mydsl_statement_block = mydsl_statement_block;
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
    public List<myDsl_Expression> getMydsl_expressions() {
        return mydsl_expressions;
    }

    public void addMydsl_expression(Mydsl_expression mydsl_expression) {
        this.mydsl_expressions.add(mydsl_expression);
    }
    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }
    public myDsl_Variable_declaration getMydsl_variable_declaration() {
        return mydsl_variable_declaration;
    }

    public void setMydsl_variable_declaration(myDsl_Variable_declaration mydsl_variable_declaration) {
        this.mydsl_variable_declaration = mydsl_variable_declaration;
    }

}