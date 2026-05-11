





import java.util.List;
import java.util.ArrayList;

public class swrtj_Expression extends GenericExpression {

    private String sign;
    private String operatorList;



    public swrtj_Expression(
        String sign,        String operatorList    ) {
        super(
        );
        this.sign = sign;
        this.operatorList = operatorList;
    }


    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }
    public String getOperatorlist() {
        return operatorList;
    }

    public void setOperatorlist(String operatorList) {
        this.operatorList = operatorList;
    }


}