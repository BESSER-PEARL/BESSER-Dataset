





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_If_Then_Else_ElseIfPart  {






    private lua_Expression lua_expression;




    private lua_Block lua_block;




    private lua_Statement_If_Then_Else lua_statement_if_then_else;


    public lua_Statement_If_Then_Else_ElseIfPart(
    ) {
    }



    public lua_Expression getLua_expression() {
        return lua_expression;
    }

    public void setLua_expression(lua_Expression lua_expression) {
        this.lua_expression = lua_expression;
    }
    public lua_Block getLua_block() {
        return lua_block;
    }

    public void setLua_block(lua_Block lua_block) {
        this.lua_block = lua_block;
    }
    public lua_Statement_If_Then_Else getLua_statement_if_then_else() {
        return lua_statement_if_then_else;
    }

    public void setLua_statement_if_then_else(lua_Statement_If_Then_Else lua_statement_if_then_else) {
        this.lua_statement_if_then_else = lua_statement_if_then_else;
    }

}