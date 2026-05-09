





import java.util.List;
import java.util.ArrayList;

public class javaMM_LabeledStatement extends NamedElement, Statement {






    private List<javaMM_BreakStatement> javamm_breakstatements;




    private javaMM_BreakStatement javamm_breakstatement;


    public javaMM_LabeledStatement(
    ) {
        super(
        );
        this.javamm_breakstatements = new ArrayList<>();
    }

    public javaMM_LabeledStatement(
        ArrayList<javaMM_BreakStatement> javamm_breakstatements    ) {
        this.javamm_breakstatements = javamm_breakstatements;
    }


    public List<javaMM_BreakStatement> getJavamm_breakstatements() {
        return javamm_breakstatements;
    }

    public void addJavamm_breakstatement(Javamm_breakstatement javamm_breakstatement) {
        this.javamm_breakstatements.add(javamm_breakstatement);
    }
    public javaMM_BreakStatement getJavamm_breakstatement() {
        return javamm_breakstatement;
    }

    public void setJavamm_breakstatement(javaMM_BreakStatement javamm_breakstatement) {
        this.javamm_breakstatement = javamm_breakstatement;
    }

}