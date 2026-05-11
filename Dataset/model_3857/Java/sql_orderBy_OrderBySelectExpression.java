





import java.util.List;
import java.util.ArrayList;

public class sql_orderBy_OrderBySelectExpression extends OrderByExpression {






    private SelectExpression selectexpression;


    public sql_orderBy_OrderBySelectExpression(
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