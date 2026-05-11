





import java.util.List;
import java.util.ArrayList;

public class frontend_core_KeywordParameter  {

    private String keyword;





    private Expression expression;


    public frontend_core_KeywordParameter(
        String keyword    ) {
        this.keyword = keyword;
    }


    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}