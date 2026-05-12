





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Value  {

    private int value;
    private String val;





    private reqLanguage_PrefixCondition reqlanguage_prefixcondition;


    public reqLanguage_Value(
        int value,        String val    ) {
        this.value = value;
        this.val = val;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getVal() {
        return val;
    }

    public void setVal(String val) {
        this.val = val;
    }

    public reqLanguage_PrefixCondition getReqlanguage_prefixcondition() {
        return reqlanguage_prefixcondition;
    }

    public void setReqlanguage_prefixcondition(reqLanguage_PrefixCondition reqlanguage_prefixcondition) {
        this.reqlanguage_prefixcondition = reqlanguage_prefixcondition;
    }

}