





import java.util.List;
import java.util.ArrayList;

public class javaDsl_SwitchStatement extends Statement {






    private List<javaDsl_BlockStatement> javadsl_blockstatements;




    private javaDsl_Expression javadsl_expression;


    public javaDsl_SwitchStatement(
    ) {
        super(
        );
        this.javadsl_blockstatements = new ArrayList<>();
    }

    public javaDsl_SwitchStatement(
        ArrayList<javaDsl_BlockStatement> javadsl_blockstatements    ) {
        this.javadsl_blockstatements = javadsl_blockstatements;
    }


    public List<javaDsl_BlockStatement> getJavadsl_blockstatements() {
        return javadsl_blockstatements;
    }

    public void addJavadsl_blockstatement(Javadsl_blockstatement javadsl_blockstatement) {
        this.javadsl_blockstatements.add(javadsl_blockstatement);
    }
    public javaDsl_Expression getJavadsl_expression() {
        return javadsl_expression;
    }

    public void setJavadsl_expression(javaDsl_Expression javadsl_expression) {
        this.javadsl_expression = javadsl_expression;
    }

}