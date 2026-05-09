





import java.util.List;
import java.util.ArrayList;

public class eol_NameExpression extends Expression {

    private boolean isType;
    private String name;
    private String resolvedContent;





    private eol_ModelDeclarationStatement eol_modeldeclarationstatement;




    private eol_NewExpression eol_newexpression;




    private eol_VariableDeclarationExpression eol_variabledeclarationexpression;




    private eol_VariableDeclarationExpression eol_variabledeclarationexpression;




    private eol_EnumerationLiteralExpression eol_enumerationliteralexpression;




    private eol_EnumerationLiteralExpression eol_enumerationliteralexpression;




    private eol_OperationDefinition eol_operationdefinition;




    private eol_EnumerationLiteralExpression eol_enumerationliteralexpression;


    public eol_NameExpression(
        boolean isType,        String name,        String resolvedContent    ) {
        super(
        );
        this.isType = isType;
        this.name = name;
        this.resolvedContent = resolvedContent;
    }


    public boolean getIstype() {
        return isType;
    }

    public void setIstype(boolean isType) {
        this.isType = isType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getResolvedcontent() {
        return resolvedContent;
    }

    public void setResolvedcontent(String resolvedContent) {
        this.resolvedContent = resolvedContent;
    }

    public eol_ModelDeclarationStatement getEol_modeldeclarationstatement() {
        return eol_modeldeclarationstatement;
    }

    public void setEol_modeldeclarationstatement(eol_ModelDeclarationStatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatement = eol_modeldeclarationstatement;
    }
    public eol_NewExpression getEol_newexpression() {
        return eol_newexpression;
    }

    public void setEol_newexpression(eol_NewExpression eol_newexpression) {
        this.eol_newexpression = eol_newexpression;
    }
    public eol_VariableDeclarationExpression getEol_variabledeclarationexpression() {
        return eol_variabledeclarationexpression;
    }

    public void setEol_variabledeclarationexpression(eol_VariableDeclarationExpression eol_variabledeclarationexpression) {
        this.eol_variabledeclarationexpression = eol_variabledeclarationexpression;
    }
    public eol_VariableDeclarationExpression getEol_variabledeclarationexpression() {
        return eol_variabledeclarationexpression;
    }

    public void setEol_variabledeclarationexpression(eol_VariableDeclarationExpression eol_variabledeclarationexpression) {
        this.eol_variabledeclarationexpression = eol_variabledeclarationexpression;
    }
    public eol_EnumerationLiteralExpression getEol_enumerationliteralexpression() {
        return eol_enumerationliteralexpression;
    }

    public void setEol_enumerationliteralexpression(eol_EnumerationLiteralExpression eol_enumerationliteralexpression) {
        this.eol_enumerationliteralexpression = eol_enumerationliteralexpression;
    }
    public eol_EnumerationLiteralExpression getEol_enumerationliteralexpression() {
        return eol_enumerationliteralexpression;
    }

    public void setEol_enumerationliteralexpression(eol_EnumerationLiteralExpression eol_enumerationliteralexpression) {
        this.eol_enumerationliteralexpression = eol_enumerationliteralexpression;
    }
    public eol_OperationDefinition getEol_operationdefinition() {
        return eol_operationdefinition;
    }

    public void setEol_operationdefinition(eol_OperationDefinition eol_operationdefinition) {
        this.eol_operationdefinition = eol_operationdefinition;
    }
    public eol_EnumerationLiteralExpression getEol_enumerationliteralexpression() {
        return eol_enumerationliteralexpression;
    }

    public void setEol_enumerationliteralexpression(eol_EnumerationLiteralExpression eol_enumerationliteralexpression) {
        this.eol_enumerationliteralexpression = eol_enumerationliteralexpression;
    }

}