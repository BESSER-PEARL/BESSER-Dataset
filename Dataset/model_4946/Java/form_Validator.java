





import java.util.List;
import java.util.ArrayList;

public class form_Validator  {

    private String validatorClass;
    private String htmlClass;
    private boolean belowField;
    private String name;



    public form_Validator(
        String validatorClass,        String htmlClass,        boolean belowField,        String name    ) {
        this.validatorClass = validatorClass;
        this.htmlClass = htmlClass;
        this.belowField = belowField;
        this.name = name;
    }


    public String getValidatorclass() {
        return validatorClass;
    }

    public void setValidatorclass(String validatorClass) {
        this.validatorClass = validatorClass;
    }
    public String getHtmlclass() {
        return htmlClass;
    }

    public void setHtmlclass(String htmlClass) {
        this.htmlClass = htmlClass;
    }
    public boolean getBelowfield() {
        return belowField;
    }

    public void setBelowfield(boolean belowField) {
        this.belowField = belowField;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}