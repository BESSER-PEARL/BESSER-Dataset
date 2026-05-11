





import java.util.List;
import java.util.ArrayList;

public class NQC_Case  {

    private boolean IsDefault;





    private List<NQC_ConstantExpression> nqc_constantexpressions;




    private NQC_SwitchStatement nqc_switchstatement;




    private List<NQC_Statement> nqc_statements;


    public NQC_Case(
        boolean IsDefault    ) {
        this.IsDefault = IsDefault;
        this.nqc_constantexpressions = new ArrayList<>();
        this.nqc_statements = new ArrayList<>();
    }

    public NQC_Case(
        boolean IsDefault        ArrayList<NQC_ConstantExpression> nqc_constantexpressions,        ArrayList<NQC_Statement> nqc_statements    ) {
        this.IsDefault = IsDefault;
        this.nqc_constantexpressions = nqc_constantexpressions;
        this.nqc_statements = nqc_statements;
    }

    public boolean getIsdefault() {
        return IsDefault;
    }

    public void setIsdefault(boolean IsDefault) {
        this.IsDefault = IsDefault;
    }

    public List<NQC_ConstantExpression> getNqc_constantexpressions() {
        return nqc_constantexpressions;
    }

    public void addNqc_constantexpression(Nqc_constantexpression nqc_constantexpression) {
        this.nqc_constantexpressions.add(nqc_constantexpression);
    }
    public NQC_SwitchStatement getNqc_switchstatement() {
        return nqc_switchstatement;
    }

    public void setNqc_switchstatement(NQC_SwitchStatement nqc_switchstatement) {
        this.nqc_switchstatement = nqc_switchstatement;
    }
    public List<NQC_Statement> getNqc_statements() {
        return nqc_statements;
    }

    public void addNqc_statement(Nqc_statement nqc_statement) {
        this.nqc_statements.add(nqc_statement);
    }

}