





import java.util.List;
import java.util.ArrayList;

public class builds_PasswordParameterDefinition extends ParameterDefinition {

    private String defaultValue;



    public builds_PasswordParameterDefinition(
        String defaultValue    ) {
        super(
        );
        this.defaultValue = defaultValue;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}