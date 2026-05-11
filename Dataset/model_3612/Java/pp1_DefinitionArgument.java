





import java.util.List;
import java.util.ArrayList;

public class pp1_DefinitionArgument  {

    private String op;
    private String argName;





    private pp1_DefinitionArgumentList pp1_definitionargumentlist;




    private pp1_Expression pp1_expression;


    public pp1_DefinitionArgument(
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

    public pp1_DefinitionArgumentList getPp1_definitionargumentlist() {
        return pp1_definitionargumentlist;
    }

    public void setPp1_definitionargumentlist(pp1_DefinitionArgumentList pp1_definitionargumentlist) {
        this.pp1_definitionargumentlist = pp1_definitionargumentlist;
    }
    public pp1_Expression getPp1_expression() {
        return pp1_expression;
    }

    public void setPp1_expression(pp1_Expression pp1_expression) {
        this.pp1_expression = pp1_expression;
    }

}