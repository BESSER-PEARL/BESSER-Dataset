





import java.util.List;
import java.util.ArrayList;

public class sql_limit_LimitExpression  {

    private String limit;
    private String offset;



    public sql_limit_LimitExpression(
        String limit,        String offset    ) {
        this.limit = limit;
        this.offset = offset;
    }


    public String getLimit() {
        return limit;
    }

    public void setLimit(String limit) {
        this.limit = limit;
    }
    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }


}