





import java.util.List;
import java.util.ArrayList;

public class imp_Block extends Stmt {






    private List<imp_Stmt> imp_stmts;


    public imp_Block(
    ) {
        super(
        );
        this.imp_stmts = new ArrayList<>();
    }

    public imp_Block(
        ArrayList<imp_Stmt> imp_stmts    ) {
        this.imp_stmts = imp_stmts;
    }


    public List<imp_Stmt> getImp_stmts() {
        return imp_stmts;
    }

    public void addImp_stmt(Imp_stmt imp_stmt) {
        this.imp_stmts.add(imp_stmt);
    }

}