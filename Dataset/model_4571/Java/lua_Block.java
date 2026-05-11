





import java.util.List;
import java.util.ArrayList;

public class lua_Block extends Chunk {






    private lua_Statement_For_Numeric lua_statement_for_numeric;




    private lua_Function lua_function;




    private lua_Statement_If_Then_Else lua_statement_if_then_else;




    private lua_Statement_Repeat lua_statement_repeat;




    private lua_Statement_For_Generic lua_statement_for_generic;




    private lua_Statement_While lua_statement_while;




    private lua_Statement_If_Then_Else_ElseIfPart lua_statement_if_then_else_elseifpart;




    private lua_LastStatement lua_laststatement;




    private lua_Statement_Block lua_statement_block;




    private lua_Statement_If_Then_Else lua_statement_if_then_else;


    public lua_Block(
    ) {
        super(
        );
    }



    public lua_Statement_For_Numeric getLua_statement_for_numeric() {
        return lua_statement_for_numeric;
    }

    public void setLua_statement_for_numeric(lua_Statement_For_Numeric lua_statement_for_numeric) {
        this.lua_statement_for_numeric = lua_statement_for_numeric;
    }
    public lua_Function getLua_function() {
        return lua_function;
    }

    public void setLua_function(lua_Function lua_function) {
        this.lua_function = lua_function;
    }
    public lua_Statement_If_Then_Else getLua_statement_if_then_else() {
        return lua_statement_if_then_else;
    }

    public void setLua_statement_if_then_else(lua_Statement_If_Then_Else lua_statement_if_then_else) {
        this.lua_statement_if_then_else = lua_statement_if_then_else;
    }
    public lua_Statement_Repeat getLua_statement_repeat() {
        return lua_statement_repeat;
    }

    public void setLua_statement_repeat(lua_Statement_Repeat lua_statement_repeat) {
        this.lua_statement_repeat = lua_statement_repeat;
    }
    public lua_Statement_For_Generic getLua_statement_for_generic() {
        return lua_statement_for_generic;
    }

    public void setLua_statement_for_generic(lua_Statement_For_Generic lua_statement_for_generic) {
        this.lua_statement_for_generic = lua_statement_for_generic;
    }
    public lua_Statement_While getLua_statement_while() {
        return lua_statement_while;
    }

    public void setLua_statement_while(lua_Statement_While lua_statement_while) {
        this.lua_statement_while = lua_statement_while;
    }
    public lua_Statement_If_Then_Else_ElseIfPart getLua_statement_if_then_else_elseifpart() {
        return lua_statement_if_then_else_elseifpart;
    }

    public void setLua_statement_if_then_else_elseifpart(lua_Statement_If_Then_Else_ElseIfPart lua_statement_if_then_else_elseifpart) {
        this.lua_statement_if_then_else_elseifpart = lua_statement_if_then_else_elseifpart;
    }
    public lua_LastStatement getLua_laststatement() {
        return lua_laststatement;
    }

    public void setLua_laststatement(lua_LastStatement lua_laststatement) {
        this.lua_laststatement = lua_laststatement;
    }
    public lua_Statement_Block getLua_statement_block() {
        return lua_statement_block;
    }

    public void setLua_statement_block(lua_Statement_Block lua_statement_block) {
        this.lua_statement_block = lua_statement_block;
    }
    public lua_Statement_If_Then_Else getLua_statement_if_then_else() {
        return lua_statement_if_then_else;
    }

    public void setLua_statement_if_then_else(lua_Statement_If_Then_Else lua_statement_if_then_else) {
        this.lua_statement_if_then_else = lua_statement_if_then_else;
    }

}