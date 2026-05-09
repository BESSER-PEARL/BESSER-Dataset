





import java.util.List;
import java.util.ArrayList;

public class morel_UnaryExp extends MultiplicativeExpChild {

    private String operator;



    public morel_UnaryExp(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}