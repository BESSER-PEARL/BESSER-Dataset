





import java.util.List;
import java.util.ArrayList;

public class query_XMLValueFunctionForest extends XMLValueFunction {

    private String returningOption;
    private String nullHandlingOption;



    public query_XMLValueFunctionForest(
        String returningOption,        String nullHandlingOption    ) {
        super(
        );
        this.returningOption = returningOption;
        this.nullHandlingOption = nullHandlingOption;
    }


    public String getReturningoption() {
        return returningOption;
    }

    public void setReturningoption(String returningOption) {
        this.returningOption = returningOption;
    }
    public String getNullhandlingoption() {
        return nullHandlingOption;
    }

    public void setNullhandlingoption(String nullHandlingOption) {
        this.nullHandlingOption = nullHandlingOption;
    }


}