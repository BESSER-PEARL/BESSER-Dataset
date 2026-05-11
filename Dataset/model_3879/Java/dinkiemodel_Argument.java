





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_Argument  {

    private String name;





    private dinkiemodel_FunctionDecl dinkiemodel_functiondecl;


    public dinkiemodel_Argument(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dinkiemodel_FunctionDecl getDinkiemodel_functiondecl() {
        return dinkiemodel_functiondecl;
    }

    public void setDinkiemodel_functiondecl(dinkiemodel_FunctionDecl dinkiemodel_functiondecl) {
        this.dinkiemodel_functiondecl = dinkiemodel_functiondecl;
    }

}