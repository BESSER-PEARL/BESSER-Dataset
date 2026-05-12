





import java.util.List;
import java.util.ArrayList;

public class query_XMLValueFunctionPI extends XMLValueFunction {

    private String targetName;
    private String returningOption;



    public query_XMLValueFunctionPI(
        String targetName,        String returningOption    ) {
        super(
        );
        this.targetName = targetName;
        this.returningOption = returningOption;
    }


    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
    }
    public String getReturningoption() {
        return returningOption;
    }

    public void setReturningoption(String returningOption) {
        this.returningOption = returningOption;
    }


}