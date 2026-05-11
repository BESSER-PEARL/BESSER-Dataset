





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsExpression extends RdbmsElement {

    private String expression;



    public rdbms_RdbmsExpression(
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