





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_If_Then_Else extends Statement {






    private List<lua_Statement_If_Then_Else_ElseIfPart> lua_statement_if_then_else_elseifparts;




    private lua_Expression lua_expression;


    public lua_Statement_If_Then_Else(
    ) {
        super(
        );
        this.lua_statement_if_then_else_elseifparts = new ArrayList<>();
    }

    public lua_Statement_If_Then_Else(
        ArrayList<lua_Statement_If_Then_Else_ElseIfPart> lua_statement_if_then_else_elseifparts    ) {
        this.lua_statement_if_then_else_elseifparts = lua_statement_if_then_else_elseifparts;
    }


    public List<lua_Statement_If_Then_Else_ElseIfPart> getLua_statement_if_then_else_elseifparts() {
        return lua_statement_if_then_else_elseifparts;
    }

    public void addLua_statement_if_then_else_elseifpart(Lua_statement_if_then_else_elseifpart lua_statement_if_then_else_elseifpart) {
        this.lua_statement_if_then_else_elseifparts.add(lua_statement_if_then_else_elseifpart);
    }
    public lua_Expression getLua_expression() {
        return lua_expression;
    }

    public void setLua_expression(lua_Expression lua_expression) {
        this.lua_expression = lua_expression;
    }

}