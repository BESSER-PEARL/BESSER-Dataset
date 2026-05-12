





import java.util.List;
import java.util.ArrayList;

public class query_XMLAggregateFunction extends ValueExpressionFunction {

    private String returningOption;



    public query_XMLAggregateFunction(
        String returningOption    ) {
        super(
        );
        this.returningOption = returningOption;
    }


    public String getReturningoption() {
        return returningOption;
    }

    public void setReturningoption(String returningOption) {
        this.returningOption = returningOption;
    }


}