





import java.util.List;
import java.util.ArrayList;

public class imp_Class extends NamedElement {

    private String name;





    private List<imp_MethodDecl> imp_methoddecls;




    private imp_NewClass imp_newclass;




    private imp_Program imp_program;


    public imp_Class(
        String name    ) {
        super(
        );
        this.name = name;
        this.imp_methoddecls = new ArrayList<>();
    }

    public imp_Class(
        String name        ArrayList<imp_MethodDecl> imp_methoddecls    ) {
        this.name = name;
        this.imp_methoddecls = imp_methoddecls;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<imp_MethodDecl> getImp_methoddecls() {
        return imp_methoddecls;
    }

    public void addImp_methoddecl(Imp_methoddecl imp_methoddecl) {
        this.imp_methoddecls.add(imp_methoddecl);
    }
    public imp_NewClass getImp_newclass() {
        return imp_newclass;
    }

    public void setImp_newclass(imp_NewClass imp_newclass) {
        this.imp_newclass = imp_newclass;
    }
    public imp_Program getImp_program() {
        return imp_program;
    }

    public void setImp_program(imp_Program imp_program) {
        this.imp_program = imp_program;
    }

}