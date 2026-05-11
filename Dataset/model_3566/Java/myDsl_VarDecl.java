





import java.util.List;
import java.util.ArrayList;

public class myDsl_VarDecl  {

    private String var;





    private myDsl_Declaration mydsl_declaration;


    public myDsl_VarDecl(
        String var    ) {
        this.var = var;
    }


    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }

    public myDsl_Declaration getMydsl_declaration() {
        return mydsl_declaration;
    }

    public void setMydsl_declaration(myDsl_Declaration mydsl_declaration) {
        this.mydsl_declaration = mydsl_declaration;
    }

}