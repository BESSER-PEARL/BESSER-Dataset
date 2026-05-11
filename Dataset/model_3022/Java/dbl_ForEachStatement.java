





import java.util.List;
import java.util.ArrayList;

public class dbl_ForEachStatement extends CompositeStatement {






    private dbl_VariableAccess dbl_variableaccess;




    private dbl_Expression dbl_expression;




    private dbl_CodeBlock dbl_codeblock;




    private dbl_Variable dbl_variable;


    public dbl_ForEachStatement(
    ) {
        super(
        );
    }



    public dbl_VariableAccess getDbl_variableaccess() {
        return dbl_variableaccess;
    }

    public void setDbl_variableaccess(dbl_VariableAccess dbl_variableaccess) {
        this.dbl_variableaccess = dbl_variableaccess;
    }
    public dbl_Expression getDbl_expression() {
        return dbl_expression;
    }

    public void setDbl_expression(dbl_Expression dbl_expression) {
        this.dbl_expression = dbl_expression;
    }
    public dbl_CodeBlock getDbl_codeblock() {
        return dbl_codeblock;
    }

    public void setDbl_codeblock(dbl_CodeBlock dbl_codeblock) {
        this.dbl_codeblock = dbl_codeblock;
    }
    public dbl_Variable getDbl_variable() {
        return dbl_variable;
    }

    public void setDbl_variable(dbl_Variable dbl_variable) {
        this.dbl_variable = dbl_variable;
    }

}