





import java.util.List;
import java.util.ArrayList;

public class arithmetic_AbstractDefinition  {

    private String name;





    private arithmetic_FunctionCall arithmetic_functioncall;


    public arithmetic_AbstractDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arithmetic_FunctionCall getArithmetic_functioncall() {
        return arithmetic_functioncall;
    }

    public void setArithmetic_functioncall(arithmetic_FunctionCall arithmetic_functioncall) {
        this.arithmetic_functioncall = arithmetic_functioncall;
    }

}