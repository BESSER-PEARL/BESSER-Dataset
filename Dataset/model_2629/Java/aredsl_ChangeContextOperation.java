





import java.util.List;
import java.util.ArrayList;

public class aredsl_ChangeContextOperation extends DomainOperation {

    private String expression;



    public aredsl_ChangeContextOperation(
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