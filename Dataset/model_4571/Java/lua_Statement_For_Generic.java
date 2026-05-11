





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_For_Generic extends Statement {

    private String names;





    private List<lua_Expression> lua_expressions;


    public lua_Statement_For_Generic(
        String names    ) {
        super(
        );
        this.names = names;
        this.lua_expressions = new ArrayList<>();
    }

    public lua_Statement_For_Generic(
        String names        ArrayList<lua_Expression> lua_expressions    ) {
        this.names = names;
        this.lua_expressions = lua_expressions;
    }

    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public List<lua_Expression> getLua_expressions() {
        return lua_expressions;
    }

    public void addLua_expression(Lua_expression lua_expression) {
        this.lua_expressions.add(lua_expression);
    }

}