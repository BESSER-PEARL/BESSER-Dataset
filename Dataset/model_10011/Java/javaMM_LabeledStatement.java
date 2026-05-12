





import java.util.List;
import java.util.ArrayList;

public class javaMM_LabeledStatement extends Statement, NamedElement {






    private javaMM_Statement javamm_statement;




    private List<javaMM_BreakStatement> javamm_breakstatements;




    private List<javaMM_ContinueStatement> javamm_continuestatements;




    private javaMM_BreakStatement javamm_breakstatement;




    private javaMM_ContinueStatement javamm_continuestatement;


    public javaMM_LabeledStatement(
    ) {
        super(
        );
        this.javamm_breakstatements = new ArrayList<>();
        this.javamm_continuestatements = new ArrayList<>();
    }

    public javaMM_LabeledStatement(
        ArrayList<javaMM_BreakStatement> javamm_breakstatements,        ArrayList<javaMM_ContinueStatement> javamm_continuestatements    ) {
        this.javamm_breakstatements = javamm_breakstatements;
        this.javamm_continuestatements = javamm_continuestatements;
    }


    public javaMM_Statement getJavamm_statement() {
        return javamm_statement;
    }

    public void setJavamm_statement(javaMM_Statement javamm_statement) {
        this.javamm_statement = javamm_statement;
    }
    public List<javaMM_BreakStatement> getJavamm_breakstatements() {
        return javamm_breakstatements;
    }

    public void addJavamm_breakstatement(Javamm_breakstatement javamm_breakstatement) {
        this.javamm_breakstatements.add(javamm_breakstatement);
    }
    public List<javaMM_ContinueStatement> getJavamm_continuestatements() {
        return javamm_continuestatements;
    }

    public void addJavamm_continuestatement(Javamm_continuestatement javamm_continuestatement) {
        this.javamm_continuestatements.add(javamm_continuestatement);
    }
    public javaMM_BreakStatement getJavamm_breakstatement() {
        return javamm_breakstatement;
    }

    public void setJavamm_breakstatement(javaMM_BreakStatement javamm_breakstatement) {
        this.javamm_breakstatement = javamm_breakstatement;
    }
    public javaMM_ContinueStatement getJavamm_continuestatement() {
        return javamm_continuestatement;
    }

    public void setJavamm_continuestatement(javaMM_ContinueStatement javamm_continuestatement) {
        this.javamm_continuestatement = javamm_continuestatement;
    }

}