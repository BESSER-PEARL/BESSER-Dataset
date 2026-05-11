





import java.util.List;
import java.util.ArrayList;

public class Java_VariableDeclaration extends Statement {

    private String variableName;



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


}