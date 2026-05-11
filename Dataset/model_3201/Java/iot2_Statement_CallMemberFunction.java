





import java.util.List;
import java.util.ArrayList;

public class iot2_Statement_CallMemberFunction extends Statement_FunctioncallOrAssignment {

    private String memberFunctionName;





    private iot2_Expression iot2_expression;


    public iot2_Statement_CallMemberFunction(
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

    public iot2_Expression getIot2_expression() {
        return iot2_expression;
    }

    public void setIot2_expression(iot2_Expression iot2_expression) {
        this.iot2_expression = iot2_expression;
    }

}