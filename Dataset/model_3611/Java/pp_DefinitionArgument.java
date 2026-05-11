





import java.util.List;
import java.util.ArrayList;

public class pp_DefinitionArgument  {

    private String argName;
    private String op;





    private pp_DefinitionArgumentList pp_definitionargumentlist;


    public pp_DefinitionArgument(
        String argName,        String op    ) {
        this.argName = argName;
        this.op = op;
    }


    public String getArgname() {
        return argName;
    }

    public void setArgname(String argName) {
        this.argName = argName;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public pp_DefinitionArgumentList getPp_definitionargumentlist() {
        return pp_definitionargumentlist;
    }

    public void setPp_definitionargumentlist(pp_DefinitionArgumentList pp_definitionargumentlist) {
        this.pp_definitionargumentlist = pp_definitionargumentlist;
    }

}