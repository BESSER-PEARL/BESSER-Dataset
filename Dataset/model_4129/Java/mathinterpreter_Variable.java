





import java.util.List;
import java.util.ArrayList;

public class mathinterpreter_Variable  {

    private String name;





    private mathinterpreter_VariableDefinition mathinterpreter_variabledefinition;




    private mathinterpreter_DefineExpr mathinterpreter_defineexpr;


    public mathinterpreter_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mathinterpreter_VariableDefinition getMathinterpreter_variabledefinition() {
        return mathinterpreter_variabledefinition;
    }

    public void setMathinterpreter_variabledefinition(mathinterpreter_VariableDefinition mathinterpreter_variabledefinition) {
        this.mathinterpreter_variabledefinition = mathinterpreter_variabledefinition;
    }
    public mathinterpreter_DefineExpr getMathinterpreter_defineexpr() {
        return mathinterpreter_defineexpr;
    }

    public void setMathinterpreter_defineexpr(mathinterpreter_DefineExpr mathinterpreter_defineexpr) {
        this.mathinterpreter_defineexpr = mathinterpreter_defineexpr;
    }

}