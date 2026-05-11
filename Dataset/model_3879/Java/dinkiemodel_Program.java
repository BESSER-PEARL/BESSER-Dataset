





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_Program  {






    private dinkiemodel_Main dinkiemodel_main;




    private List<dinkiemodel_FunctionDecl> dinkiemodel_functiondecls;


    public dinkiemodel_Program(
    ) {
        this.dinkiemodel_functiondecls = new ArrayList<>();
    }

    public dinkiemodel_Program(
        ArrayList<dinkiemodel_FunctionDecl> dinkiemodel_functiondecls    ) {
        this.dinkiemodel_functiondecls = dinkiemodel_functiondecls;
    }


    public dinkiemodel_Main getDinkiemodel_main() {
        return dinkiemodel_main;
    }

    public void setDinkiemodel_main(dinkiemodel_Main dinkiemodel_main) {
        this.dinkiemodel_main = dinkiemodel_main;
    }
    public List<dinkiemodel_FunctionDecl> getDinkiemodel_functiondecls() {
        return dinkiemodel_functiondecls;
    }

    public void addDinkiemodel_functiondecl(Dinkiemodel_functiondecl dinkiemodel_functiondecl) {
        this.dinkiemodel_functiondecls.add(dinkiemodel_functiondecl);
    }

}