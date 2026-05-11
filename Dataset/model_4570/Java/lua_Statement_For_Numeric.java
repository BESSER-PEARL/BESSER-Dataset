





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_For_Numeric extends Statement {

    private String iteratorName;





    private lua_Block lua_block;


    public lua_Statement_For_Numeric(
        String iteratorName    ) {
        super(
        );
        this.iteratorName = iteratorName;
    }


    public String getIteratorname() {
        return iteratorName;
    }

    public void setIteratorname(String iteratorName) {
        this.iteratorName = iteratorName;
    }

    public lua_Block getLua_block() {
        return lua_block;
    }

    public void setLua_block(lua_Block lua_block) {
        this.lua_block = lua_block;
    }

}