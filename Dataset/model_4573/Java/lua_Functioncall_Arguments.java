





import java.util.List;
import java.util.ArrayList;

public class lua_Functioncall_Arguments  {






    private lua_Expression_CallFunction lua_expression_callfunction;




    private List<lua_Expression> lua_expressions;




    private lua_Expression_CallMemberFunction lua_expression_callmemberfunction;




    private lua_Statement_CallFunction lua_statement_callfunction;




    private lua_Statement_CallMemberFunction lua_statement_callmemberfunction;


    public lua_Functioncall_Arguments(
    ) {
        this.lua_expressions = new ArrayList<>();
    }

    public lua_Functioncall_Arguments(
        ArrayList<lua_Expression> lua_expressions    ) {
        this.lua_expressions = lua_expressions;
    }


    public lua_Expression_CallFunction getLua_expression_callfunction() {
        return lua_expression_callfunction;
    }

    public void setLua_expression_callfunction(lua_Expression_CallFunction lua_expression_callfunction) {
        this.lua_expression_callfunction = lua_expression_callfunction;
    }
    public List<lua_Expression> getLua_expressions() {
        return lua_expressions;
    }

    public void addLua_expression(Lua_expression lua_expression) {
        this.lua_expressions.add(lua_expression);
    }
    public lua_Expression_CallMemberFunction getLua_expression_callmemberfunction() {
        return lua_expression_callmemberfunction;
    }

    public void setLua_expression_callmemberfunction(lua_Expression_CallMemberFunction lua_expression_callmemberfunction) {
        this.lua_expression_callmemberfunction = lua_expression_callmemberfunction;
    }
    public lua_Statement_CallFunction getLua_statement_callfunction() {
        return lua_statement_callfunction;
    }

    public void setLua_statement_callfunction(lua_Statement_CallFunction lua_statement_callfunction) {
        this.lua_statement_callfunction = lua_statement_callfunction;
    }
    public lua_Statement_CallMemberFunction getLua_statement_callmemberfunction() {
        return lua_statement_callmemberfunction;
    }

    public void setLua_statement_callmemberfunction(lua_Statement_CallMemberFunction lua_statement_callmemberfunction) {
        this.lua_statement_callmemberfunction = lua_statement_callmemberfunction;
    }

}