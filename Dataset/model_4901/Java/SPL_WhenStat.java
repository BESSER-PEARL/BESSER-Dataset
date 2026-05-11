





import java.util.List;
import java.util.ArrayList;

public class SPL_WhenStat extends Statement {






    private List<SPL_Statement> spl_statements;




    private SPL_Variable spl_variable;




    private List<SPL_WhenHeader> spl_whenheaders;




    private List<SPL_Statement> spl_statements;


    public SPL_WhenStat(
    ) {
        super(
        );
        this.spl_statements = new ArrayList<>();
        this.spl_whenheaders = new ArrayList<>();
        this.spl_statements = new ArrayList<>();
    }

    public SPL_WhenStat(
        ArrayList<SPL_Statement> spl_statements,        ArrayList<SPL_WhenHeader> spl_whenheaders,        ArrayList<SPL_Statement> spl_statements    ) {
        this.spl_statements = spl_statements;
        this.spl_whenheaders = spl_whenheaders;
        this.spl_statements = spl_statements;
    }


    public List<SPL_Statement> getSpl_statements() {
        return spl_statements;
    }

    public void addSpl_statement(Spl_statement spl_statement) {
        this.spl_statements.add(spl_statement);
    }
    public SPL_Variable getSpl_variable() {
        return spl_variable;
    }

    public void setSpl_variable(SPL_Variable spl_variable) {
        this.spl_variable = spl_variable;
    }
    public List<SPL_WhenHeader> getSpl_whenheaders() {
        return spl_whenheaders;
    }

    public void addSpl_whenheader(Spl_whenheader spl_whenheader) {
        this.spl_whenheaders.add(spl_whenheader);
    }
    public List<SPL_Statement> getSpl_statements() {
        return spl_statements;
    }

    public void addSpl_statement(Spl_statement spl_statement) {
        this.spl_statements.add(spl_statement);
    }

}