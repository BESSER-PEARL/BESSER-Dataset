





import java.util.List;
import java.util.ArrayList;

public class eol_ModelDeclarationStatement extends Statement {

    private String resolvedIMetamodel;





    private List<eol_ModelDeclarationParameter> eol_modeldeclarationparameters;




    private eol_NameExpression eol_nameexpression;




    private List<eol_VariableDeclarationExpression> eol_variabledeclarationexpressions;




    private eol_VariableDeclarationExpression eol_variabledeclarationexpression;


    public eol_ModelDeclarationStatement(
        String resolvedIMetamodel    ) {
        super(
        );
        this.resolvedIMetamodel = resolvedIMetamodel;
        this.eol_modeldeclarationparameters = new ArrayList<>();
        this.eol_variabledeclarationexpressions = new ArrayList<>();
    }

    public eol_ModelDeclarationStatement(
        String resolvedIMetamodel        ArrayList<eol_ModelDeclarationParameter> eol_modeldeclarationparameters,        ArrayList<eol_VariableDeclarationExpression> eol_variabledeclarationexpressions    ) {
        this.resolvedIMetamodel = resolvedIMetamodel;
        this.eol_modeldeclarationparameters = eol_modeldeclarationparameters;
        this.eol_variabledeclarationexpressions = eol_variabledeclarationexpressions;
    }

    public String getResolvedimetamodel() {
        return resolvedIMetamodel;
    }

    public void setResolvedimetamodel(String resolvedIMetamodel) {
        this.resolvedIMetamodel = resolvedIMetamodel;
    }

    public List<eol_ModelDeclarationParameter> getEol_modeldeclarationparameters() {
        return eol_modeldeclarationparameters;
    }

    public void addEol_modeldeclarationparameter(Eol_modeldeclarationparameter eol_modeldeclarationparameter) {
        this.eol_modeldeclarationparameters.add(eol_modeldeclarationparameter);
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }
    public List<eol_VariableDeclarationExpression> getEol_variabledeclarationexpressions() {
        return eol_variabledeclarationexpressions;
    }

    public void addEol_variabledeclarationexpression(Eol_variabledeclarationexpression eol_variabledeclarationexpression) {
        this.eol_variabledeclarationexpressions.add(eol_variabledeclarationexpression);
    }
    public eol_VariableDeclarationExpression getEol_variabledeclarationexpression() {
        return eol_variabledeclarationexpression;
    }

    public void setEol_variabledeclarationexpression(eol_VariableDeclarationExpression eol_variabledeclarationexpression) {
        this.eol_variabledeclarationexpression = eol_variabledeclarationexpression;
    }

}