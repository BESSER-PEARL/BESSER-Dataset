





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_LocalFunction_Declaration extends Statement {

    private String functionName;





    private lua_Function lua_function;


    public lua_Statement_LocalFunction_Declaration(
        String functionName    ) {
        super(
        );
        this.functionName = functionName;
    }


    public String getFunctionname() {
        return functionName;
    }

    public void setFunctionname(String functionName) {
        this.functionName = functionName;
    }

    public lua_Function getLua_function() {
        return lua_function;
    }

    public void setLua_function(lua_Function lua_function) {
        this.lua_function = lua_function;
    }

}