





import java.util.List;
import java.util.ArrayList;

public class eol_ModelDeclarationStatement extends Statement {






    private eol_NameExpression eol_nameexpression;




    private List<eol_NameExpression> eol_nameexpressions;




    private eol_ModelDeclarationStatement eol_modeldeclarationstatement;




    private eol_NameExpression eol_nameexpression;


    public eol_ModelDeclarationStatement(
    ) {
        super(
        );
        this.eol_nameexpressions = new ArrayList<>();
    }

    public eol_ModelDeclarationStatement(
        ArrayList<eol_NameExpression> eol_nameexpressions    ) {
        this.eol_nameexpressions = eol_nameexpressions;
    }


    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }
    public List<eol_NameExpression> getEol_nameexpressions() {
        return eol_nameexpressions;
    }

    public void addEol_nameexpression(Eol_nameexpression eol_nameexpression) {
        this.eol_nameexpressions.add(eol_nameexpression);
    }
    public eol_ModelDeclarationStatement getEol_modeldeclarationstatement() {
        return eol_modeldeclarationstatement;
    }

    public void setEol_modeldeclarationstatement(eol_ModelDeclarationStatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatement = eol_modeldeclarationstatement;
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }

}