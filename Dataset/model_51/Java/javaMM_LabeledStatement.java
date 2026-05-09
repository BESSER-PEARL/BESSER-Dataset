





import java.util.List;
import java.util.ArrayList;

public class javaMM_LabeledStatement extends NamedElement, Statement {






    private List<javaMM_ContinueStatement> javamm_continuestatements;




    private javaMM_ContinueStatement javamm_continuestatement;




    private javaMM_Statement javamm_statement;


    public javaMM_LabeledStatement(
    ) {
        super(
        );
        this.javamm_continuestatements = new ArrayList<>();
    }

    public javaMM_LabeledStatement(
        ArrayList<javaMM_ContinueStatement> javamm_continuestatements    ) {
        this.javamm_continuestatements = javamm_continuestatements;
    }


    public List<javaMM_ContinueStatement> getJavamm_continuestatements() {
        return javamm_continuestatements;
    }

    public void addJavamm_continuestatement(Javamm_continuestatement javamm_continuestatement) {
        this.javamm_continuestatements.add(javamm_continuestatement);
    }
    public javaMM_ContinueStatement getJavamm_continuestatement() {
        return javamm_continuestatement;
    }

    public void setJavamm_continuestatement(javaMM_ContinueStatement javamm_continuestatement) {
        this.javamm_continuestatement = javamm_continuestatement;
    }
    public javaMM_Statement getJavamm_statement() {
        return javamm_statement;
    }

    public void setJavamm_statement(javaMM_Statement javamm_statement) {
        this.javamm_statement = javamm_statement;
    }

}