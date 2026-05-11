





import java.util.List;
import java.util.ArrayList;

public class arithmetics_AbstractDefinition  {

    private String name;





    private arithmetics_FunctionCall arithmetics_functioncall;


    public arithmetics_AbstractDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arithmetics_FunctionCall getArithmetics_functioncall() {
        return arithmetics_functioncall;
    }

    public void setArithmetics_functioncall(arithmetics_FunctionCall arithmetics_functioncall) {
        this.arithmetics_functioncall = arithmetics_functioncall;
    }

}