





import java.util.List;
import java.util.ArrayList;

public class morel_RelationalExp extends BooleanAndExpChild {

    private String operator;



    public morel_RelationalExp(
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