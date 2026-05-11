





import java.util.List;
import java.util.ArrayList;

public class lua_Function  {

    private boolean varArgs;
    private String parameters;





    private lua_Statement_GlobalFunction_Declaration lua_statement_globalfunction_declaration;


    public lua_Function(
        boolean varArgs,        String parameters    ) {
        this.varArgs = varArgs;
        this.parameters = parameters;
    }


    public boolean getVarargs() {
        return varArgs;
    }

    public void setVarargs(boolean varArgs) {
        this.varArgs = varArgs;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }

    public lua_Statement_GlobalFunction_Declaration getLua_statement_globalfunction_declaration() {
        return lua_statement_globalfunction_declaration;
    }

    public void setLua_statement_globalfunction_declaration(lua_Statement_GlobalFunction_Declaration lua_statement_globalfunction_declaration) {
        this.lua_statement_globalfunction_declaration = lua_statement_globalfunction_declaration;
    }

}