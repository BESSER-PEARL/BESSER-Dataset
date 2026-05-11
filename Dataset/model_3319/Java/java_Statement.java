





import java.util.List;
import java.util.ArrayList;

public class java_Statement  {

    private String name;





    private java_Variable_declaration java_variable_declaration;




    private java_Expression java_expression;




    private java_Statement_block java_statement_block;




    private java_Statement java_statement;


    public java_Statement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public java_Variable_declaration getJava_variable_declaration() {
        return java_variable_declaration;
    }

    public void setJava_variable_declaration(java_Variable_declaration java_variable_declaration) {
        this.java_variable_declaration = java_variable_declaration;
    }
    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }
    public java_Statement_block getJava_statement_block() {
        return java_statement_block;
    }

    public void setJava_statement_block(java_Statement_block java_statement_block) {
        this.java_statement_block = java_statement_block;
    }
    public java_Statement getJava_statement() {
        return java_statement;
    }

    public void setJava_statement(java_Statement java_statement) {
        this.java_statement = java_statement;
    }

}