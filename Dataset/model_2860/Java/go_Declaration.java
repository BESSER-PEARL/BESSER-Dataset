





import java.util.List;
import java.util.ArrayList;

public class go_Declaration  {






    private go_Statement go_statement;




    private go_TopLevelDecl go_topleveldecl;


    public go_Declaration(
    ) {
    }



    public go_Statement getGo_statement() {
        return go_statement;
    }

    public void setGo_statement(go_Statement go_statement) {
        this.go_statement = go_statement;
    }
    public go_TopLevelDecl getGo_topleveldecl() {
        return go_topleveldecl;
    }

    public void setGo_topleveldecl(go_TopLevelDecl go_topleveldecl) {
        this.go_topleveldecl = go_topleveldecl;
    }

}