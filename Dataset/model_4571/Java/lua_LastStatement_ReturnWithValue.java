





import java.util.List;
import java.util.ArrayList;

public class lua_LastStatement_ReturnWithValue extends LastStatement_Return {






    private List<lua_Expression> lua_expressions;


    public lua_LastStatement_ReturnWithValue(
    ) {
        super(
        );
        this.lua_expressions = new ArrayList<>();
    }

    public lua_LastStatement_ReturnWithValue(
        ArrayList<lua_Expression> lua_expressions    ) {
        this.lua_expressions = lua_expressions;
    }


    public List<lua_Expression> getLua_expressions() {
        return lua_expressions;
    }

    public void addLua_expression(Lua_expression lua_expression) {
        this.lua_expressions.add(lua_expression);
    }

}