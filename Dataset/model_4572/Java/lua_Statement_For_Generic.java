





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_For_Generic extends Statement {

    private String names;





    private lua_Block lua_block;


    public lua_Statement_For_Generic(
        String names    ) {
        super(
        );
        this.names = names;
    }


    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public lua_Block getLua_block() {
        return lua_block;
    }

    public void setLua_block(lua_Block lua_block) {
        this.lua_block = lua_block;
    }

}