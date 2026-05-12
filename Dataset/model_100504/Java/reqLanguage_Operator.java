





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Operator  {

    private String operator;





    private reqLanguage_PrefixCondition reqlanguage_prefixcondition;


    public reqLanguage_Operator(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public reqLanguage_PrefixCondition getReqlanguage_prefixcondition() {
        return reqlanguage_prefixcondition;
    }

    public void setReqlanguage_prefixcondition(reqLanguage_PrefixCondition reqlanguage_prefixcondition) {
        this.reqlanguage_prefixcondition = reqlanguage_prefixcondition;
    }

}