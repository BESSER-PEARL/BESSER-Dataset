





import java.util.List;
import java.util.ArrayList;

public class whileDsl_Input  {

    private String variables;





    private whileDsl_Definition whiledsl_definition;


    public whileDsl_Input(
        String variables    ) {
        this.variables = variables;
    }


    public String getVariables() {
        return variables;
    }

    public void setVariables(String variables) {
        this.variables = variables;
    }

    public whileDsl_Definition getWhiledsl_definition() {
        return whiledsl_definition;
    }

    public void setWhiledsl_definition(whileDsl_Definition whiledsl_definition) {
        this.whiledsl_definition = whiledsl_definition;
    }

}