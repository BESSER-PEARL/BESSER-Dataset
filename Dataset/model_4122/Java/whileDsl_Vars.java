





import java.util.List;
import java.util.ArrayList;

public class whileDsl_Vars  {

    private String variables;





    private whileDsl_VarsCommand whiledsl_varscommand;


    public whileDsl_Vars(
        String variables    ) {
        this.variables = variables;
    }


    public String getVariables() {
        return variables;
    }

    public void setVariables(String variables) {
        this.variables = variables;
    }

    public whileDsl_VarsCommand getWhiledsl_varscommand() {
        return whiledsl_varscommand;
    }

    public void setWhiledsl_varscommand(whileDsl_VarsCommand whiledsl_varscommand) {
        this.whiledsl_varscommand = whiledsl_varscommand;
    }

}