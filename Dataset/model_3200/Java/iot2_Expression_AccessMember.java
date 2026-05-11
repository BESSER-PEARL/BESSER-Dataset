





import java.util.List;
import java.util.ArrayList;

public class iot2_Expression_AccessMember extends Expression {

    private String memberName;





    private iot2_Expression iot2_expression;


    public iot2_Expression_AccessMember(
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

    public iot2_Expression getIot2_expression() {
        return iot2_expression;
    }

    public void setIot2_expression(iot2_Expression iot2_expression) {
        this.iot2_expression = iot2_expression;
    }

}