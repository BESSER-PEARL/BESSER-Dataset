





import java.util.List;
import java.util.ArrayList;

public class odemcustom_ForEachStatement extends CompositeStatement {






    private odemcustom_Variable odemcustom_variable;




    private odemcustom_Expression odemcustom_expression;




    private odemcustom_CodeBlock odemcustom_codeblock;




    private odemcustom_VariableAccess odemcustom_variableaccess;


    public odemcustom_ForEachStatement(
    ) {
        super(
        );
    }



    public odemcustom_Variable getOdemcustom_variable() {
        return odemcustom_variable;
    }

    public void setOdemcustom_variable(odemcustom_Variable odemcustom_variable) {
        this.odemcustom_variable = odemcustom_variable;
    }
    public odemcustom_Expression getOdemcustom_expression() {
        return odemcustom_expression;
    }

    public void setOdemcustom_expression(odemcustom_Expression odemcustom_expression) {
        this.odemcustom_expression = odemcustom_expression;
    }
    public odemcustom_CodeBlock getOdemcustom_codeblock() {
        return odemcustom_codeblock;
    }

    public void setOdemcustom_codeblock(odemcustom_CodeBlock odemcustom_codeblock) {
        this.odemcustom_codeblock = odemcustom_codeblock;
    }
    public odemcustom_VariableAccess getOdemcustom_variableaccess() {
        return odemcustom_variableaccess;
    }

    public void setOdemcustom_variableaccess(odemcustom_VariableAccess odemcustom_variableaccess) {
        this.odemcustom_variableaccess = odemcustom_variableaccess;
    }

}