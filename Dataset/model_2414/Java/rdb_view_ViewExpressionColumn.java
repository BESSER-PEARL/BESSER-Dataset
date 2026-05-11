





import java.util.List;
import java.util.ArrayList;

public class rdb_view_ViewExpressionColumn extends ViewColumn {

    private String expression;



    public rdb_view_ViewExpressionColumn(
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