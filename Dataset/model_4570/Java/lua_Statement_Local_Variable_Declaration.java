





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_Local_Variable_Declaration extends Statement {

    private String variableNames;



    public lua_Statement_Local_Variable_Declaration(
        String variableNames    ) {
        super(
        );
        this.variableNames = variableNames;
    }


    public String getVariablenames() {
        return variableNames;
    }

    public void setVariablenames(String variableNames) {
        this.variableNames = variableNames;
    }


}