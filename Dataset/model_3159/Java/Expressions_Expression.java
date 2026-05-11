





import java.util.List;
import java.util.ArrayList;

public class Expressions_Expression  {






    private C_Declarations_ConstantDeclaration c_declarations_constantdeclaration;




    private C_Expressions_FunctionCall c_expressions_functioncall;




    private C_Declarations_SimpleVariableDeclaration c_declarations_simplevariabledeclaration;


    public Expressions_Expression(
    ) {
    }



    public C_Declarations_ConstantDeclaration getC_declarations_constantdeclaration() {
        return c_declarations_constantdeclaration;
    }

    public void setC_declarations_constantdeclaration(C_Declarations_ConstantDeclaration c_declarations_constantdeclaration) {
        this.c_declarations_constantdeclaration = c_declarations_constantdeclaration;
    }
    public C_Expressions_FunctionCall getC_expressions_functioncall() {
        return c_expressions_functioncall;
    }

    public void setC_expressions_functioncall(C_Expressions_FunctionCall c_expressions_functioncall) {
        this.c_expressions_functioncall = c_expressions_functioncall;
    }
    public C_Declarations_SimpleVariableDeclaration getC_declarations_simplevariabledeclaration() {
        return c_declarations_simplevariabledeclaration;
    }

    public void setC_declarations_simplevariabledeclaration(C_Declarations_SimpleVariableDeclaration c_declarations_simplevariabledeclaration) {
        this.c_declarations_simplevariabledeclaration = c_declarations_simplevariabledeclaration;
    }

}