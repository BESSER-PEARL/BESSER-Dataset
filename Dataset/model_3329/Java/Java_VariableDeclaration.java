





import java.util.List;
import java.util.ArrayList;

public class Java_VariableDeclaration extends Statement {

    private String variableName;





    private Type type;


    public Java_VariableDeclaration(
        String variableName    ) {
        super(
        );
        this.variableName = variableName;
    }


    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}