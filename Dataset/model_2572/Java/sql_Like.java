





import java.util.List;
import java.util.ArrayList;

public class sql_Like  {

    private String opLike;





    private sql_FullExpression sql_fullexpression;


    public sql_Like(
        String opLike    ) {
        this.opLike = opLike;
    }


    public String getOplike() {
        return opLike;
    }

    public void setOplike(String opLike) {
        this.opLike = opLike;
    }

    public sql_FullExpression getSql_fullexpression() {
        return sql_fullexpression;
    }

    public void setSql_fullexpression(sql_FullExpression sql_fullexpression) {
        this.sql_fullexpression = sql_fullexpression;
    }

}