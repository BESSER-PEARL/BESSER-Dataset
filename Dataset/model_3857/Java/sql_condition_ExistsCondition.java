





import java.util.List;
import java.util.ArrayList;

public class sql_condition_ExistsCondition extends SimpleCondition {






    private SelectExpression selectexpression;


    public sql_condition_ExistsCondition(
    ) {
        super(
        );
    }



    public SelectExpression getSelectexpression() {
        return selectexpression;
    }

    public void setSelectexpression(SelectExpression selectexpression) {
        this.selectexpression = selectexpression;
    }

}