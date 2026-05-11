





import java.util.List;
import java.util.ArrayList;

public class builds_ChoiceParameterDefinition extends ParameterDefinition {

    private String defaultValue;
    private String options;



    public builds_ChoiceParameterDefinition(
        String defaultValue,        String options    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.options = options;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getOptions() {
        return options;
    }

    public void setOptions(String options) {
        this.options = options;
    }


}