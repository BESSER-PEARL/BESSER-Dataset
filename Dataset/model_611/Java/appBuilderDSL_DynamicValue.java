





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_DynamicValue extends Value, SetInstructionAssignment {

    private String variableName;
    private String type;



    public appBuilderDSL_DynamicValue(
        String variableName,        String type    ) {
        super(
        );
        this.variableName = variableName;
        this.type = type;
    }


    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}