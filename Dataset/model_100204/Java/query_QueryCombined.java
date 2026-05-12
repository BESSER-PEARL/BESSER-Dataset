





import java.util.List;
import java.util.ArrayList;

public class query_QueryCombined extends QueryExpressionBody {

    private String combinedOperator;



    public query_QueryCombined(
        String combinedOperator    ) {
        super(
        );
        this.combinedOperator = combinedOperator;
    }


    public String getCombinedoperator() {
        return combinedOperator;
    }

    public void setCombinedoperator(String combinedOperator) {
        this.combinedOperator = combinedOperator;
    }


}