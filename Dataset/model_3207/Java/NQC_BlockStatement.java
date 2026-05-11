





import java.util.List;
import java.util.ArrayList;

public class NQC_BlockStatement extends Statement {






    private List<NQC_LocalVariable> nqc_localvariables;




    private List<NQC_Statement> nqc_statements;


    public NQC_BlockStatement(
    ) {
        super(
        );
        this.nqc_localvariables = new ArrayList<>();
        this.nqc_statements = new ArrayList<>();
    }

    public NQC_BlockStatement(
        ArrayList<NQC_LocalVariable> nqc_localvariables,        ArrayList<NQC_Statement> nqc_statements    ) {
        this.nqc_localvariables = nqc_localvariables;
        this.nqc_statements = nqc_statements;
    }


    public List<NQC_LocalVariable> getNqc_localvariables() {
        return nqc_localvariables;
    }

    public void addNqc_localvariable(Nqc_localvariable nqc_localvariable) {
        this.nqc_localvariables.add(nqc_localvariable);
    }
    public List<NQC_Statement> getNqc_statements() {
        return nqc_statements;
    }

    public void addNqc_statement(Nqc_statement nqc_statement) {
        this.nqc_statements.add(nqc_statement);
    }

}