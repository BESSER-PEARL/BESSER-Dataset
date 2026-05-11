





import java.util.List;
import java.util.ArrayList;

public class expressions_Function  {

    private String name;





    private expressions_FunctionCall expressions_functioncall;


    public expressions_Function(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public expressions_FunctionCall getExpressions_functioncall() {
        return expressions_functioncall;
    }

    public void setExpressions_functioncall(expressions_FunctionCall expressions_functioncall) {
        this.expressions_functioncall = expressions_functioncall;
    }

}