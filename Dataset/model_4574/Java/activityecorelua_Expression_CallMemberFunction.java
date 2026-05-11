





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_Expression_CallMemberFunction extends Expression {

    private String memberFunctionName;



    public activityecorelua_Expression_CallMemberFunction(
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


}