





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_CheckAction extends Action {

    private String operator;



    public DiagonosticModel_CheckAction(
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