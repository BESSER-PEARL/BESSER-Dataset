





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_Statement_CallMemberFunction extends Statement_FunctioncallOrAssignment {

    private String memberFunctionName;





    private activityecorelua_Expression activityecorelua_expression;


    public activityecorelua_Statement_CallMemberFunction(
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

    public activityecorelua_Expression getActivityecorelua_expression() {
        return activityecorelua_expression;
    }

    public void setActivityecorelua_expression(activityecorelua_Expression activityecorelua_expression) {
        this.activityecorelua_expression = activityecorelua_expression;
    }

}