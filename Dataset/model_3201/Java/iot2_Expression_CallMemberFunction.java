





import java.util.List;
import java.util.ArrayList;

public class iot2_Expression_CallMemberFunction extends Expression {

    private String memberFunctionName;



    public iot2_Expression_CallMemberFunction(
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