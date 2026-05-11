





import java.util.List;
import java.util.ArrayList;

public class executionTrace_VariableModification extends Execution {

    private String variableName;
    private String value;



    public executionTrace_VariableModification(
        String variableName,        String value    ) {
        super(
        );
        this.variableName = variableName;
        this.value = value;
    }


    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}