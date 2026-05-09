





import java.util.List;
import java.util.ArrayList;

public class morel_AdditiveExp extends RelationalExpChild {

    private String operators;



    public morel_AdditiveExp(
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