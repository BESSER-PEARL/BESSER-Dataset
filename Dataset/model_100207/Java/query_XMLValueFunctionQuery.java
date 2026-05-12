





import java.util.List;
import java.util.ArrayList;

public class query_XMLValueFunctionQuery extends XMLValueFunction {

    private String emptyHandlingOption;



    public query_XMLValueFunctionQuery(
        String emptyHandlingOption    ) {
        super(
        );
        this.emptyHandlingOption = emptyHandlingOption;
    }


    public String getEmptyhandlingoption() {
        return emptyHandlingOption;
    }

    public void setEmptyhandlingoption(String emptyHandlingOption) {
        this.emptyHandlingOption = emptyHandlingOption;
    }


}