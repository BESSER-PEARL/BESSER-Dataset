





import java.util.List;
import java.util.ArrayList;

public class morel_BooleanOrExp extends BooleanImpliesExpChild {

    private String operators;



    public morel_BooleanOrExp(
        String operators    ) {
        super(
        );
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }


}