





import java.util.List;
import java.util.ArrayList;

public class pp2_DefinitionArgument  {

    private String op;
    private String argName;





    private pp2_DefinitionArgumentList pp2_definitionargumentlist;


    public pp2_DefinitionArgument(
        String op,        String argName    ) {
        this.op = op;
        this.argName = argName;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getArgname() {
        return argName;
    }

    public void setArgname(String argName) {
        this.argName = argName;
    }

    public pp2_DefinitionArgumentList getPp2_definitionargumentlist() {
        return pp2_definitionargumentlist;
    }

    public void setPp2_definitionargumentlist(pp2_DefinitionArgumentList pp2_definitionargumentlist) {
        this.pp2_definitionargumentlist = pp2_definitionargumentlist;
    }

}