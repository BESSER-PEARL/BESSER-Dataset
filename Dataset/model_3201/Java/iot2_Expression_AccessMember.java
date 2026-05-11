





import java.util.List;
import java.util.ArrayList;

public class iot2_Expression_AccessMember extends Expression {

    private String memberName;



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


}