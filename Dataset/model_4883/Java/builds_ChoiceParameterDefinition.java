





import java.util.List;
import java.util.ArrayList;

public class builds_ChoiceParameterDefinition extends ParameterDefinition {

    private String options;
    private String defaultValue;



    public builds_ChoiceParameterDefinition(
        String options,        String defaultValue    ) {
        super(
        );
        this.options = options;
        this.defaultValue = defaultValue;
    }


    public String getOptions() {
        return options;
    }

    public void setOptions(String options) {
        this.options = options;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}