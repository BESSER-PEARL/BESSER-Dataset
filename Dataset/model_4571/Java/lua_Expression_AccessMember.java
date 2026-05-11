





import java.util.List;
import java.util.ArrayList;

public class lua_Expression_AccessMember extends Expression {

    private String memberName;





    private lua_Expression lua_expression;


    public lua_Expression_AccessMember(
        String memberName    ) {
        super(
        );
        this.memberName = memberName;
    }


    public String getMembername() {
        return memberName;
    }

    public void setMembername(String memberName) {
        this.memberName = memberName;
    }

    public lua_Expression getLua_expression() {
        return lua_expression;
    }

    public void setLua_expression(lua_Expression lua_expression) {
        this.lua_expression = lua_expression;
    }

}