





import java.util.List;
import java.util.ArrayList;

public class EFM_Requires extends FMConstraint {

    private String operator;



    public EFM_Requires(
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