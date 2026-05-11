





import java.util.List;
import java.util.ArrayList;

public class lua_Function  {

    private String parameters;
    private boolean varArgs;





    private lua_Expression_Function lua_expression_function;




    private lua_Statement_GlobalFunction_Declaration lua_statement_globalfunction_declaration;




    private lua_Block lua_block;




    private lua_Statement_LocalFunction_Declaration lua_statement_localfunction_declaration;


    public lua_Function(
        String parameters,        boolean varArgs    ) {
        this.parameters = parameters;
        this.varArgs = varArgs;
    }


    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }
    public boolean getVarargs() {
        return varArgs;
    }

    public void setVarargs(boolean varArgs) {
        this.varArgs = varArgs;
    }

    public lua_Expression_Function getLua_expression_function() {
        return lua_expression_function;
    }

    public void setLua_expression_function(lua_Expression_Function lua_expression_function) {
        this.lua_expression_function = lua_expression_function;
    }
    public lua_Statement_GlobalFunction_Declaration getLua_statement_globalfunction_declaration() {
        return lua_statement_globalfunction_declaration;
    }

    public void setLua_statement_globalfunction_declaration(lua_Statement_GlobalFunction_Declaration lua_statement_globalfunction_declaration) {
        this.lua_statement_globalfunction_declaration = lua_statement_globalfunction_declaration;
    }
    public lua_Block getLua_block() {
        return lua_block;
    }

    public void setLua_block(lua_Block lua_block) {
        this.lua_block = lua_block;
    }
    public lua_Statement_LocalFunction_Declaration getLua_statement_localfunction_declaration() {
        return lua_statement_localfunction_declaration;
    }

    public void setLua_statement_localfunction_declaration(lua_Statement_LocalFunction_Declaration lua_statement_localfunction_declaration) {
        this.lua_statement_localfunction_declaration = lua_statement_localfunction_declaration;
    }

}