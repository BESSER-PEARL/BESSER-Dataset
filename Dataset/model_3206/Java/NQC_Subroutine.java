





import java.util.List;
import java.util.ArrayList;

public class NQC_Subroutine  {

    private String Name;





    private NQC_Program nqc_program;




    private List<NQC_Statement> nqc_statements;




    private List<NQC_LocalVariable> nqc_localvariables;


    public NQC_Subroutine(
        String Name    ) {
        this.Name = Name;
        this.nqc_statements = new ArrayList<>();
        this.nqc_localvariables = new ArrayList<>();
    }

    public NQC_Subroutine(
        String Name        ArrayList<NQC_Statement> nqc_statements,        ArrayList<NQC_LocalVariable> nqc_localvariables    ) {
        this.Name = Name;
        this.nqc_statements = nqc_statements;
        this.nqc_localvariables = nqc_localvariables;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public NQC_Program getNqc_program() {
        return nqc_program;
    }

    public void setNqc_program(NQC_Program nqc_program) {
        this.nqc_program = nqc_program;
    }
    public List<NQC_Statement> getNqc_statements() {
        return nqc_statements;
    }

    public void addNqc_statement(Nqc_statement nqc_statement) {
        this.nqc_statements.add(nqc_statement);
    }
    public List<NQC_LocalVariable> getNqc_localvariables() {
        return nqc_localvariables;
    }

    public void addNqc_localvariable(Nqc_localvariable nqc_localvariable) {
        this.nqc_localvariables.add(nqc_localvariable);
    }

}