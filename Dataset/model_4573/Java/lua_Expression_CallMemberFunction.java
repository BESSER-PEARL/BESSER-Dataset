





import java.util.List;
import java.util.ArrayList;

public class lua_Expression_CallMemberFunction extends Expression {

    private String memberFunctionName;





    private lua_Expression lua_expression;


    public lua_Expression_CallMemberFunction(
        String memberFunctionName    ) {
        super(
        );
        this.memberFunctionName = memberFunctionName;
    }


    public String getMemberfunctionname() {
        return memberFunctionName;
    }

    public void setMemberfunctionname(String memberFunctionName) {
        this.memberFunctionName = memberFunctionName;
    }

    public lua_Expression getLua_expression() {
        return lua_expression;
    }

    public void setLua_expression(lua_Expression lua_expression) {
        this.lua_expression = lua_expression;
    }

}