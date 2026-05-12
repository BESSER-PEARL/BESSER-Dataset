





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_ParamEvent  {

    private String action;





    private reqLanguage_Value reqlanguage_value;




    private reqLanguage_EObject reqlanguage_eobject;


    public reqLanguage_ParamEvent(
        String action    ) {
        this.action = action;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public reqLanguage_Value getReqlanguage_value() {
        return reqlanguage_value;
    }

    public void setReqlanguage_value(reqLanguage_Value reqlanguage_value) {
        this.reqlanguage_value = reqlanguage_value;
    }
    public reqLanguage_EObject getReqlanguage_eobject() {
        return reqlanguage_eobject;
    }

    public void setReqlanguage_eobject(reqLanguage_EObject reqlanguage_eobject) {
        this.reqlanguage_eobject = reqlanguage_eobject;
    }

}