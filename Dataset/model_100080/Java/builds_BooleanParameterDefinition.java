





import java.util.List;
import java.util.ArrayList;

public class builds_BooleanParameterDefinition extends ParameterDefinition {

    private boolean defaultValue;



    public builds_BooleanParameterDefinition(
        boolean defaultValue    ) {
        super(
        );
        this.defaultValue = defaultValue;
    }


    public boolean getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(boolean defaultValue) {
        this.defaultValue = defaultValue;
    }


}