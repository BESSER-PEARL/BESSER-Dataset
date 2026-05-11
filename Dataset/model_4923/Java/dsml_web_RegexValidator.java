





import java.util.List;
import java.util.ArrayList;

public class dsml_web_RegexValidator extends Validator {

    private String regex;



    public dsml_web_RegexValidator(
        String regex    ) {
        super(
        );
        this.regex = regex;
    }


    public String getRegex() {
        return regex;
    }

    public void setRegex(String regex) {
        this.regex = regex;
    }


}