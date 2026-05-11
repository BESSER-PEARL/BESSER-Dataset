





import java.util.List;
import java.util.ArrayList;

public class sql_from_FromExpression  {






    private List<from_TableListExpression> from_tablelistexpressions;


    public sql_from_FromExpression(
    ) {
        this.from_tablelistexpressions = new ArrayList<>();
    }

    public sql_from_FromExpression(
        ArrayList<from_TableListExpression> from_tablelistexpressions    ) {
        this.from_tablelistexpressions = from_tablelistexpressions;
    }


    public List<from_TableListExpression> getFrom_tablelistexpressions() {
        return from_tablelistexpressions;
    }

    public void addFrom_tablelistexpression(From_tablelistexpression from_tablelistexpression) {
        this.from_tablelistexpressions.add(from_tablelistexpression);
    }

}