





import java.util.List;
import java.util.ArrayList;

public class pp1_BinaryOpExpression extends BinaryExpression {

    private String opName;



    public pp1_BinaryOpExpression(
        String opName    ) {
        super(
        );
        this.opName = opName;
    }


    public String getOpname() {
        return opName;
    }

    public void setOpname(String opName) {
        this.opName = opName;
    }


}