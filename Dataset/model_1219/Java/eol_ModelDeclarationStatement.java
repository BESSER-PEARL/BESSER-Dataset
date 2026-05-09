





import java.util.List;
import java.util.ArrayList;

public class eol_ModelDeclarationStatement extends Statement {






    private List<eol_ModelDeclarationParameter> eol_modeldeclarationparameters;




    private eol_ModelType eol_modeltype;




    private List<eol_VariableDeclarationExpression> eol_variabledeclarationexpressions;




    private eol_EolLibraryModule eol_eollibrarymodule;




    private eol_VariableDeclarationExpression eol_variabledeclarationexpression;




    private eol_ModelElementType eol_modelelementtype;




    private eol_VariableDeclarationExpression eol_variabledeclarationexpression;




    private eol_ModelDeclarationStatement eol_modeldeclarationstatement;


    public eol_ModelDeclarationStatement(
    ) {
        super(
        );
        this.eol_modeldeclarationparameters = new ArrayList<>();
        this.eol_variabledeclarationexpressions = new ArrayList<>();
    }

    public eol_ModelDeclarationStatement(
        ArrayList<eol_ModelDeclarationParameter> eol_modeldeclarationparameters,        ArrayList<eol_VariableDeclarationExpression> eol_variabledeclarationexpressions    ) {
        this.eol_modeldeclarationparameters = eol_modeldeclarationparameters;
        this.eol_variabledeclarationexpressions = eol_variabledeclarationexpressions;
    }


    public List<eol_ModelDeclarationParameter> getEol_modeldeclarationparameters() {
        return eol_modeldeclarationparameters;
    }

    public void addEol_modeldeclarationparameter(Eol_modeldeclarationparameter eol_modeldeclarationparameter) {
        this.eol_modeldeclarationparameters.add(eol_modeldeclarationparameter);
    }
    public eol_ModelType getEol_modeltype() {
        return eol_modeltype;
    }

    public void setEol_modeltype(eol_ModelType eol_modeltype) {
        this.eol_modeltype = eol_modeltype;
    }
    public List<eol_VariableDeclarationExpression> getEol_variabledeclarationexpressions() {
        return eol_variabledeclarationexpressions;
    }

    public void addEol_variabledeclarationexpression(Eol_variabledeclarationexpression eol_variabledeclarationexpression) {
        this.eol_variabledeclarationexpressions.add(eol_variabledeclarationexpression);
    }
    public eol_EolLibraryModule getEol_eollibrarymodule() {
        return eol_eollibrarymodule;
    }

    public void setEol_eollibrarymodule(eol_EolLibraryModule eol_eollibrarymodule) {
        this.eol_eollibrarymodule = eol_eollibrarymodule;
    }
    public eol_VariableDeclarationExpression getEol_variabledeclarationexpression() {
        return eol_variabledeclarationexpression;
    }

    public void setEol_variabledeclarationexpression(eol_VariableDeclarationExpression eol_variabledeclarationexpression) {
        this.eol_variabledeclarationexpression = eol_variabledeclarationexpression;
    }
    public eol_ModelElementType getEol_modelelementtype() {
        return eol_modelelementtype;
    }

    public void setEol_modelelementtype(eol_ModelElementType eol_modelelementtype) {
        this.eol_modelelementtype = eol_modelelementtype;
    }
    public eol_VariableDeclarationExpression getEol_variabledeclarationexpression() {
        return eol_variabledeclarationexpression;
    }

    public void setEol_variabledeclarationexpression(eol_VariableDeclarationExpression eol_variabledeclarationexpression) {
        this.eol_variabledeclarationexpression = eol_variabledeclarationexpression;
    }
    public eol_ModelDeclarationStatement getEol_modeldeclarationstatement() {
        return eol_modeldeclarationstatement;
    }

    public void setEol_modeldeclarationstatement(eol_ModelDeclarationStatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatement = eol_modeldeclarationstatement;
    }

}