





import java.util.List;
import java.util.ArrayList;

public class query_XMLValueFunctionConcat extends XMLValueFunction {

    private String returningOption;



    public query_XMLValueFunctionConcat(
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