





import java.util.List;
import java.util.ArrayList;

public class imp_MethodDecl extends Member {

    private String name;





    private List<imp_ParamDecl> imp_paramdecls;




    private imp_Program imp_program;




    private imp_Stmt imp_stmt;


    public imp_MethodDecl(
        String name    ) {
        super(
        );
        this.name = name;
        this.imp_paramdecls = new ArrayList<>();
    }

    public imp_MethodDecl(
        String name        ArrayList<imp_ParamDecl> imp_paramdecls    ) {
        this.name = name;
        this.imp_paramdecls = imp_paramdecls;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<imp_ParamDecl> getImp_paramdecls() {
        return imp_paramdecls;
    }

    public void addImp_paramdecl(Imp_paramdecl imp_paramdecl) {
        this.imp_paramdecls.add(imp_paramdecl);
    }
    public imp_Program getImp_program() {
        return imp_program;
    }

    public void setImp_program(imp_Program imp_program) {
        this.imp_program = imp_program;
    }
    public imp_Stmt getImp_stmt() {
        return imp_stmt;
    }

    public void setImp_stmt(imp_Stmt imp_stmt) {
        this.imp_stmt = imp_stmt;
    }

}