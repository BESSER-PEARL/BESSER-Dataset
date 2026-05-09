





import java.util.List;
import java.util.ArrayList;

public class eol_VariableDeclarationExpression extends Expression {

    private boolean create;





    private List<eol_NameExpression> eol_nameexpressions;




    private eol_ModelDeclarationStatement eol_modeldeclarationstatement;




    private List<eol_Expression> eol_expressions;




    private eol_OperationDefinition eol_operationdefinition;




    private eol_OperationDefinition eol_operationdefinition;




    private eol_ModelDeclarationStatement eol_modeldeclarationstatement;




    private eol_NameExpression eol_nameexpression;


    public eol_VariableDeclarationExpression(
        boolean create    ) {
        super(
        );
        this.create = create;
        this.eol_nameexpressions = new ArrayList<>();
        this.eol_expressions = new ArrayList<>();
    }

    public eol_VariableDeclarationExpression(
        boolean create        ArrayList<eol_NameExpression> eol_nameexpressions,        ArrayList<eol_Expression> eol_expressions    ) {
        this.create = create;
        this.eol_nameexpressions = eol_nameexpressions;
        this.eol_expressions = eol_expressions;
    }

    public boolean getCreate() {
        return create;
    }

    public void setCreate(boolean create) {
        this.create = create;
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
    public List<eol_Expression> getEol_expressions() {
        return eol_expressions;
    }

    public void addEol_expression(Eol_expression eol_expression) {
        this.eol_expressions.add(eol_expression);
    }
    public eol_OperationDefinition getEol_operationdefinition() {
        return eol_operationdefinition;
    }

    public void setEol_operationdefinition(eol_OperationDefinition eol_operationdefinition) {
        this.eol_operationdefinition = eol_operationdefinition;
    }
    public eol_OperationDefinition getEol_operationdefinition() {
        return eol_operationdefinition;
    }

    public void setEol_operationdefinition(eol_OperationDefinition eol_operationdefinition) {
        this.eol_operationdefinition = eol_operationdefinition;
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