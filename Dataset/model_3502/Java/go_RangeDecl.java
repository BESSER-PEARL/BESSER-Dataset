





import java.util.List;
import java.util.ArrayList;

public class go_RangeDecl  {






    private go_FunctionCall go_functioncall;




    private go_VarCall go_varcall;




    private go_IGUAL go_igual;




    private go_PONTOSIGUAL go_pontosigual;




    private List<go_IDList> go_idlists;




    private go_ForDecl go_fordecl;


    public go_RangeDecl(
    ) {
        this.go_idlists = new ArrayList<>();
    }

    public go_RangeDecl(
        ArrayList<go_IDList> go_idlists    ) {
        this.go_idlists = go_idlists;
    }


    public go_FunctionCall getGo_functioncall() {
        return go_functioncall;
    }

    public void setGo_functioncall(go_FunctionCall go_functioncall) {
        this.go_functioncall = go_functioncall;
    }
    public go_VarCall getGo_varcall() {
        return go_varcall;
    }

    public void setGo_varcall(go_VarCall go_varcall) {
        this.go_varcall = go_varcall;
    }
    public go_IGUAL getGo_igual() {
        return go_igual;
    }

    public void setGo_igual(go_IGUAL go_igual) {
        this.go_igual = go_igual;
    }
    public go_PONTOSIGUAL getGo_pontosigual() {
        return go_pontosigual;
    }

    public void setGo_pontosigual(go_PONTOSIGUAL go_pontosigual) {
        this.go_pontosigual = go_pontosigual;
    }
    public List<go_IDList> getGo_idlists() {
        return go_idlists;
    }

    public void addGo_idlist(Go_idlist go_idlist) {
        this.go_idlists.add(go_idlist);
    }
    public go_ForDecl getGo_fordecl() {
        return go_fordecl;
    }

    public void setGo_fordecl(go_ForDecl go_fordecl) {
        this.go_fordecl = go_fordecl;
    }

}