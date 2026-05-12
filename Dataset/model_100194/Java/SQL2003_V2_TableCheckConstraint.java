





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_TableCheckConstraint extends TableConstraint {

    private String expression;



    public SQL2003_V2_TableCheckConstraint(
        String expression    ) {
        super(
        );
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}