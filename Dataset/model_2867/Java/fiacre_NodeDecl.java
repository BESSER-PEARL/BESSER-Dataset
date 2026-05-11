





import java.util.List;
import java.util.ArrayList;

public class fiacre_NodeDecl extends Declaration {






    private fiacre_Statement fiacre_statement;




    private fiacre_Program fiacre_program;




    private List<fiacre_LocalPortDecl> fiacre_localportdecls;




    private List<fiacre_LocalVariable> fiacre_localvariables;




    private List<fiacre_ArgumentVariable> fiacre_argumentvariables;




    private List<fiacre_ParamPortDecl> fiacre_paramportdecls;


    public fiacre_NodeDecl(
    ) {
        super(
        );
        this.fiacre_localportdecls = new ArrayList<>();
        this.fiacre_localvariables = new ArrayList<>();
        this.fiacre_argumentvariables = new ArrayList<>();
        this.fiacre_paramportdecls = new ArrayList<>();
    }

    public fiacre_NodeDecl(
        ArrayList<fiacre_LocalPortDecl> fiacre_localportdecls,        ArrayList<fiacre_LocalVariable> fiacre_localvariables,        ArrayList<fiacre_ArgumentVariable> fiacre_argumentvariables,        ArrayList<fiacre_ParamPortDecl> fiacre_paramportdecls    ) {
        this.fiacre_localportdecls = fiacre_localportdecls;
        this.fiacre_localvariables = fiacre_localvariables;
        this.fiacre_argumentvariables = fiacre_argumentvariables;
        this.fiacre_paramportdecls = fiacre_paramportdecls;
    }


    public fiacre_Statement getFiacre_statement() {
        return fiacre_statement;
    }

    public void setFiacre_statement(fiacre_Statement fiacre_statement) {
        this.fiacre_statement = fiacre_statement;
    }
    public fiacre_Program getFiacre_program() {
        return fiacre_program;
    }

    public void setFiacre_program(fiacre_Program fiacre_program) {
        this.fiacre_program = fiacre_program;
    }
    public List<fiacre_LocalPortDecl> getFiacre_localportdecls() {
        return fiacre_localportdecls;
    }

    public void addFiacre_localportdecl(Fiacre_localportdecl fiacre_localportdecl) {
        this.fiacre_localportdecls.add(fiacre_localportdecl);
    }
    public List<fiacre_LocalVariable> getFiacre_localvariables() {
        return fiacre_localvariables;
    }

    public void addFiacre_localvariable(Fiacre_localvariable fiacre_localvariable) {
        this.fiacre_localvariables.add(fiacre_localvariable);
    }
    public List<fiacre_ArgumentVariable> getFiacre_argumentvariables() {
        return fiacre_argumentvariables;
    }

    public void addFiacre_argumentvariable(Fiacre_argumentvariable fiacre_argumentvariable) {
        this.fiacre_argumentvariables.add(fiacre_argumentvariable);
    }
    public List<fiacre_ParamPortDecl> getFiacre_paramportdecls() {
        return fiacre_paramportdecls;
    }

    public void addFiacre_paramportdecl(Fiacre_paramportdecl fiacre_paramportdecl) {
        this.fiacre_paramportdecls.add(fiacre_paramportdecl);
    }

}