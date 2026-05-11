





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_Assignment extends Statement_FunctioncallOrAssignment {






    private List<lua_Expression> lua_expressions;




    private List<lua_Expression> lua_expressions;


    public lua_Statement_Assignment(
    ) {
        super(
        );
        this.lua_expressions = new ArrayList<>();
        this.lua_expressions = new ArrayList<>();
    }

    public lua_Statement_Assignment(
        ArrayList<lua_Expression> lua_expressions,        ArrayList<lua_Expression> lua_expressions    ) {
        this.lua_expressions = lua_expressions;
        this.lua_expressions = lua_expressions;
    }


    public List<lua_Expression> getLua_expressions() {
        return lua_expressions;
    }

    public void addLua_expression(Lua_expression lua_expression) {
        this.lua_expressions.add(lua_expression);
    }
    public List<lua_Expression> getLua_expressions() {
        return lua_expressions;
    }

    public void addLua_expression(Lua_expression lua_expression) {
        this.lua_expressions.add(lua_expression);
    }

}