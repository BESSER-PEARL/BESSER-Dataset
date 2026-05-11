





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_Local_Variable_Declaration extends Statement {

    private String variableNames;





    private List<lua_Expression> lua_expressions;


    public lua_Statement_Local_Variable_Declaration(
        String variableNames    ) {
        super(
        );
        this.variableNames = variableNames;
        this.lua_expressions = new ArrayList<>();
    }

    public lua_Statement_Local_Variable_Declaration(
        String variableNames        ArrayList<lua_Expression> lua_expressions    ) {
        this.variableNames = variableNames;
        this.lua_expressions = lua_expressions;
    }

    public String getVariablenames() {
        return variableNames;
    }

    public void setVariablenames(String variableNames) {
        this.variableNames = variableNames;
    }

    public List<lua_Expression> getLua_expressions() {
        return lua_expressions;
    }

    public void addLua_expression(Lua_expression lua_expression) {
        this.lua_expressions.add(lua_expression);
    }

}