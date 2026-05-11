





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_PrefixRightOperand  {

    private String operator;





    private reqLanguage_Prefix reqlanguage_prefix;




    private reqLanguage_EObject reqlanguage_eobject;


    public reqLanguage_PrefixRightOperand(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public reqLanguage_Prefix getReqlanguage_prefix() {
        return reqlanguage_prefix;
    }

    public void setReqlanguage_prefix(reqLanguage_Prefix reqlanguage_prefix) {
        this.reqlanguage_prefix = reqlanguage_prefix;
    }
    public reqLanguage_EObject getReqlanguage_eobject() {
        return reqlanguage_eobject;
    }

    public void setReqlanguage_eobject(reqLanguage_EObject reqlanguage_eobject) {
        this.reqlanguage_eobject = reqlanguage_eobject;
    }

}