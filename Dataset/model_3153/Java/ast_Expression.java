





import java.util.List;
import java.util.ArrayList;

public class ast_Expression  {






    private ast_Equation ast_equation;




    private ast_Assertion ast_assertion;




    private ast_Equation ast_equation;




    private ast_VariableDeclaration ast_variabledeclaration;




    private ast_FunctionObjectDeclaration ast_functionobjectdeclaration;




    private ast_Assertion ast_assertion;




    private ast_IterationAccumulator ast_iterationaccumulator;




    private ast_Check ast_check;


    public ast_Expression(
    ) {
    }



    public ast_Equation getAst_equation() {
        return ast_equation;
    }

    public void setAst_equation(ast_Equation ast_equation) {
        this.ast_equation = ast_equation;
    }
    public ast_Assertion getAst_assertion() {
        return ast_assertion;
    }

    public void setAst_assertion(ast_Assertion ast_assertion) {
        this.ast_assertion = ast_assertion;
    }
    public ast_Equation getAst_equation() {
        return ast_equation;
    }

    public void setAst_equation(ast_Equation ast_equation) {
        this.ast_equation = ast_equation;
    }
    public ast_VariableDeclaration getAst_variabledeclaration() {
        return ast_variabledeclaration;
    }

    public void setAst_variabledeclaration(ast_VariableDeclaration ast_variabledeclaration) {
        this.ast_variabledeclaration = ast_variabledeclaration;
    }
    public ast_FunctionObjectDeclaration getAst_functionobjectdeclaration() {
        return ast_functionobjectdeclaration;
    }

    public void setAst_functionobjectdeclaration(ast_FunctionObjectDeclaration ast_functionobjectdeclaration) {
        this.ast_functionobjectdeclaration = ast_functionobjectdeclaration;
    }
    public ast_Assertion getAst_assertion() {
        return ast_assertion;
    }

    public void setAst_assertion(ast_Assertion ast_assertion) {
        this.ast_assertion = ast_assertion;
    }
    public ast_IterationAccumulator getAst_iterationaccumulator() {
        return ast_iterationaccumulator;
    }

    public void setAst_iterationaccumulator(ast_IterationAccumulator ast_iterationaccumulator) {
        this.ast_iterationaccumulator = ast_iterationaccumulator;
    }
    public ast_Check getAst_check() {
        return ast_check;
    }

    public void setAst_check(ast_Check ast_check) {
        this.ast_check = ast_check;
    }

}