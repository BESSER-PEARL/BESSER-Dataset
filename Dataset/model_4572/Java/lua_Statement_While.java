





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_While extends Statement {






    private lua_Block lua_block;


    public lua_Statement_While(
    ) {
        super(
        );
    }



    public lua_Block getLua_block() {
        return lua_block;
    }

    public void setLua_block(lua_Block lua_block) {
        this.lua_block = lua_block;
    }

}