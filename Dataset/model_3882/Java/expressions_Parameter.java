





import java.util.List;
import java.util.ArrayList;

public class expressions_Parameter  {

    private String name;





    private expressions_Function expressions_function;




    private expressions_ParameterAccess expressions_parameteraccess;


    public expressions_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public expressions_Function getExpressions_function() {
        return expressions_function;
    }

    public void setExpressions_function(expressions_Function expressions_function) {
        this.expressions_function = expressions_function;
    }
    public expressions_ParameterAccess getExpressions_parameteraccess() {
        return expressions_parameteraccess;
    }

    public void setExpressions_parameteraccess(expressions_ParameterAccess expressions_parameteraccess) {
        this.expressions_parameteraccess = expressions_parameteraccess;
    }

}