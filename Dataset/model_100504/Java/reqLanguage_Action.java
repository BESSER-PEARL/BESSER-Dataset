





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Action  {

    private String name;
    private String action;





    private reqLanguage_Parameter reqlanguage_parameter;




    private reqLanguage_Value reqlanguage_value;




    private reqLanguage_EObject reqlanguage_eobject;




    private reqLanguage_MainFunction reqlanguage_mainfunction;


    public reqLanguage_Action(
        String name,        String action    ) {
        this.name = name;
        this.action = action;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public reqLanguage_Parameter getReqlanguage_parameter() {
        return reqlanguage_parameter;
    }

    public void setReqlanguage_parameter(reqLanguage_Parameter reqlanguage_parameter) {
        this.reqlanguage_parameter = reqlanguage_parameter;
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
    public reqLanguage_MainFunction getReqlanguage_mainfunction() {
        return reqlanguage_mainfunction;
    }

    public void setReqlanguage_mainfunction(reqLanguage_MainFunction reqlanguage_mainfunction) {
        this.reqlanguage_mainfunction = reqlanguage_mainfunction;
    }

}